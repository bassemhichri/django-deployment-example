from django import forms
from django.contrib.auth.models import User
from my_app.models import UserPI

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserPI_Form(forms.ModelForm):

    class Meta():
        model = UserPI
        fields = ('portfolio_site','profile_pic')
