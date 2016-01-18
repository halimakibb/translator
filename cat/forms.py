from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm
#from tinymce.widgets import TinyMCE
from models import User, OriginalArticle, TranslatedArticle

class MyRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name')
        
    def save(self, commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
    
        if commit:
            user.save()
    
        return user 
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = OriginalArticle
        fields = ('title', 'body')
        widgets = {'title': Textarea(attrs={'rows': '2'}),
                   'body': Textarea(attrs={'rows': '10'})}
        
class TranslateForm(forms.ModelForm):
    class Meta:
        model = TranslatedArticle
        fields = ('title', 'body')
        widgets = {'title': Textarea(attrs={'rows': '2'}),
                   'body': Textarea(attrs={'rows': '10'})}        
        
                   
       