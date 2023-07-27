from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class' : 'form_control', 'placeholder' : 'Как к вам обращаться'})) 
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class' : 'form_control', 'placeholder' : 'Ваш e-mail'}))
    messengers = forms.CharField(label='Мессенджеры', widget=forms.TextInput(attrs={'class' : 'form_control', 'placeholder' : 'Telegram, Viber, VK и т.д.'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class' : 'form_control', 'placeholder' : '+375(..)...-..-..'}))
    captcha = CaptchaField()
