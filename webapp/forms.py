from re import T
from django import forms

class PostForm(forms.Form):
    cUserName = forms.CharField(max_length=255, initial='', required=True)
    cUserAccount = forms.CharField(max_length=255, initial='', required=True)
    cUserPassword = forms.CharField(widget=forms.PasswordInput(), max_length=255, initial='', required=True)
    cUserPicture = forms.CharField(max_length=255, initial='None', required=False)
    cUserStyle = forms.CharField(max_length=255, initial='', required=False)
    cUserScore = forms.CharField(max_length=255, initial='', required=False)
    cUserStuff = forms.CharField(max_length=255, initial='', required=False)
    cUserTemporarilyScore = forms.CharField(max_length=255, initial='', required=False)