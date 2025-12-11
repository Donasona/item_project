from django import forms
from user_app.models import Item
from django.contrib.auth.models import User

class Formitem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password']

# class Loginform(forms.Form):
#     username = forms.CharField(max_length=20)
#     password = forms.CharField()
