import email
from enum import unique
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Reviews
from django.forms import Textarea
from captcha.fields import CaptchaField


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class' : 'form_control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class' : 'form_control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class' : 'form_control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class' : 'form_control'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class' : 'form_control', 'placeholder' : 'Введите ваше имя пользователя'}))
    password =forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class' : 'form_control', 'placeholder' : 'Введите ваш пароль'}))

class UserPasswordChangeForm(PasswordChangeForm):
    old_password =forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class' : 'form_control', 'placeholder' : 'Введите ваш пароль'}))
    new_password1 =forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class' : 'form_control', 'placeholder' : 'Введите ваш новый пароль'}))
    new_password2 =forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class' : 'form_control', 'placeholder' : 'Подтвердите ваш новый пароль'}))
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['text']
        widgets = {
        'text': Textarea(attrs={'class' : 'form_control', 'placeholder' : 'Длина комментария не должна превышать 500 символов'})
        }

class EmailChangeForm(forms.Form):
    email = forms.EmailField(label='Старый email', widget=forms.EmailInput(attrs={'class' : 'form_control'}))
    email1 = forms.EmailField(label='Новый email', widget=forms.EmailInput(attrs={'class' : 'form_control'}))
    email2 = forms.EmailField(label='Подтвердите email', widget=forms.EmailInput(attrs={'class' : 'form_control'}))
    captcha = CaptchaField()
    error_messages = {
    'not_changed': ("Введённый email совпадаат с имеющемся"),
    'email_mismatch': ("Два поля адресов электронной почты не совпадают"),
    }
    class Meta:
        model = User
        fields = ('email', 'email1', 'email2')
