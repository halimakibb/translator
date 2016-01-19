from django.shortcuts import render, render_to_response
from .models import User, OriginalArticle, TranslatedArticle, TranslatedManager
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from .forms import ArticleForm, TranslateForm, MyRegistrationForm

# Create your views here.

def wordcount(text):
    text_list = text.split(' ')
    return len(text_list)

def index(request):
    try: 
        request.session['user_id']
        job = request.user.job
        if job == "CL":
            return HttpResponseRedirect('/cat/client_dashboard')
        elif job == "TR":
            return HttpResponseRedirect('/cat/translator_dashboard')
        else:
            return render_to_response('cat/index.html')
    except:
        return render_to_response('cat/index.html')

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('cat/login.html', c)

def auth_view(request):
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(name=name, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/cat/loggedin')
    else:
        return render(request, 'cat/invalid.html')

def loggedin(request):
    request.session['user_id'] = request.user.id
    request.session.set_expiry(0)
    return render_to_response('cat/logged_in.html',
                              {'full_name': request.user.name})

def logout(request):
    auth.logout(request)
    return render_to_response('cat/logout.html')


def register(request, jobcode):
    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            if jobcode == "client":
                user.job = "CL"
                user.save()
            elif jobcode == "translator":
                user.job == "TR"
                user.save()
            else:
                return HttpResponse(jobcode)
            return render(request, 'cat/register_success.html')
        else:
            return render(request, 'cat/invalid.html')
    else:
        args = {}
        args.update(csrf(request))
        
        args['form'] = MyRegistrationForm()
        args['jobcode'] = jobcode
        
        return render_to_response('cat/register.html', args)

def register_success(request):
    return render(request, 'cat/register_success.html')

def unassigned(request):
    article_list = OriginalArticle.objects.filter(is_assigned=False)
    return render_to_response('cat/unassigned.html', 
                              {'article_list': article_list})

def assign_translator(request, article_id):
    article = OriginalArticle.objects.get(id = article_id)
    if article.is_assigned == False:
        translators = User.objects.filter(job = "TR")
        return render_to_response('cat/assign.html',
                                  {'translators': translators,
                                   'article': article})
    else:
        return HttpResponse("This article has already been assigned")

def assigned(request, article_id, translator_id):
    
    
    original = OriginalArticle.objects.get(id = article_id)
    original.is_assigned = True
    original.save()
    translator = User.objects.get(id = translator_id)
    article = TranslatedArticle.objects.create_article(original, translator)
        
    return render_to_response('cat/assigned.html',
                              {'article': original,
                               'translator': translator})

def create_article(request):
    RATE = 0.05

    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        
        if form.is_valid():
            article = form.save(commit = False)
            words1 = article.title
            words2 = article.body
            totalwords = wordcount(words1) + wordcount(words2)
            totalprice = totalwords * RATE
            request.session['title'] = words1
            request.session['body'] = words2
            request.session['totalwords'] = totalwords
            request.session['totalprice'] = totalprice
            #return render_to_response('cat/success.html',
                                      #{'title': article.title,
                                       #'totalwords': totalwords,
                                       #'totalprice': totalprice})
            return HttpResponseRedirect('/cat/confirm_article')
        else:
            return render_to_response('cat/invalid.html')
    else:
        form = ArticleForm()

        args = {}
        args.update(csrf(request))

        args['form'] = form

        return render_to_response('cat/create_article.html', args)

def confirm_article(request):
    title = request.session['title']
    body = request.session['body']
    totalwords = request.session['totalwords']
    totalprice = request.session['totalprice']

    
    return render_to_response('cat/confirm.html',
                              {'title': title,
                               'totalwords': totalwords,
                               'totalprice': totalprice})

def confirm_yes(request):
    title = request.session['title']
    body = request.session['body']
    totalwords = request.session['totalwords']
    totalprice = request.session['totalprice']
    
    article = OriginalArticle.objects.create_article(title, body, totalwords, 
                                                    totalprice)
    
    del request.session['title']
    del request.session['body']
    del request.session['totalwords']
    del request.session['totalprice']
    
    return render_to_response('cat/confirm_yes.html',
                              {'title': title,
                               'totalwords': totalwords,
                               'totalprice': totalprice})

def confirm_no(request):
    del request.session['title']
    del request.session['body']
    del request.session['totalwords']
    del request.session['totalprice']
    
    return render_to_response('cat/confirm_no.html')

def untranslated(request):
    try:
        request.session['user_id']
        translator = request.user.id
        if request.user.job == "TR":
            article_list = TranslatedArticle.objects.filter(is_translated=False, translator = translator)
            return render_to_response('cat/untranslated.html',
                                      {'article_list': article_list})
        else:
            return render_to_response('cat/invalid.html')
    except:
        return render_to_response('cat/invalid.html')
            

def translate(request, article_id):
    if request.POST:
        translated = TranslatedArticle.objects.get(id = article_id)
        form = TranslateForm(request.POST)
        if form.is_valid():
            article = form.save(commit = False)
            translated.title = article.title
            translated.body = article.body
            translated.is_translated = True
            translated.save()
            return HttpResponse('udah ditranslate')
        else:
            return render_to_response('cat/invalid.html')
    else:
        translated = TranslatedArticle.objects.get(id = article_id)
        original = translated.origin        
        form = TranslateForm(instance=translated)
        title = form['title']
        body = form['body']

        args = {}
        args.update(csrf(request))

        args['form'] = form
        args['original'] = original
        args['title'] = title
        args['body'] = body
        
        return render_to_response('cat/translate.html',
                                  args) 

def client_dashboard(request):
    try: 
        request.session['user_id']
        name = request.user.name
        job = request.user.job
        if job == "CL":
            return render(request, 'cat/client_dashboard.html', 
                          {'name': name})
        else:
            return render(request, 'cat/invalid.html')
    except:
        return render(request, 'cat/invalid.html')
    
def translator_dashboard(request):
    try:
        request.session['user_id']
        name = request.user.name
        job = request.user.job
        if job == "TR":
            return render(request, 'cat/translator_dashboard.html',
                          {'name': name})
        else:
            return render(request, 'cat/invalid.html')
    except:
        return render(request, 'cat/invalid.html')