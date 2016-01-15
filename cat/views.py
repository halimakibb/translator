from django.shortcuts import render, render_to_response
from .models import User, OriginalArticle, TranslatedArticle
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf

# Create your views here.

def index(request):
    return render_to_response('cat/index.html')

def register(request):
    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cat/register_success')
        else:
            return HttpResponseRedirect('/cat/invalid')
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = MyRegistrationForm()
    
    return render_to_response('cat/register.html', args)