from django.shortcuts import render, render_to_response
from .models import User, OriginalArticle, TranslatedArticle, TranslatedManager
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from .forms import ArticleForm, TranslateForm

# Create your views here.

def wordcount(text):
    text_list = text.split(' ')
    return len(text_list)

def index(request):
    return render_to_response('cat/index.html')

def register(request):
    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('cat/register_success')
        else:
            return HttpResponseRedirect('cat/invalid')
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = MyRegistrationForm()
    
    return render_to_response('cat/register.html', args)

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
            article.word_count = totalwords
            article.price = totalprice
            article.save()
            return render_to_response('cat/success.html',
                                      {'title': article.title,
                                       'totalwords': totalwords,
                                       'totalprice': totalprice})
        else:
            return render_to_response('cat/invalid.html')
    else:
        form = ArticleForm()

        args = {}
        args.update(csrf(request))

        args['form'] = form

        return render_to_response('cat/create_article.html', args)

def untranslated(request):
    article_list = OriginalArticle.objects.filter(is_translated=False)
    return render_to_response('cat/untranslated.html',
                              {'article_list': article_list})

def translate(request, article_id):
    if request.POST:
        translated = TranslatedArticle.objects.get(origin = article_id)
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
        translated = TranslatedArticle.objects.get(origin = article_id)
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
