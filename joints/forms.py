from django import forms
#from .models import Joint

class EmailForm(forms.Form):
    name=forms.CharField(required=False)
    email=forms.EmailField()
    #email=forms.EmailField()

