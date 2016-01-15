from django import forms
from django.contrib.auth.forms import UserCreationForm
#from tinymce.widgets import TinyMCE
from models import User

class MyRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name')
        
    def save(self, commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
    
        if commit:
            user.save()
    
        return user 