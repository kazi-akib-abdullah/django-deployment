from django import forms
from django.contrib.auth.models import User
from django.db.models.aggregates import Min
from django.forms import fields
from Login_app.models import UserInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6)
    email = forms.EmailField(widget=forms.EmailInput(), required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserInfoForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=True)
    class Meta:
        model = UserInfo
        fields = ('facebook_id','profile_pic')