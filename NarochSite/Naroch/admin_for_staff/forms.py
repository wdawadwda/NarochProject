from user.models import Reviews
from gallery.models import Photo
from django.forms import ModelForm
from django import forms

class ReviewsAdminFrom(ModelForm):
    text = forms.Textarea(attrs={'class' : 'form_control', 'placeholder' : 'Длина комментария не должна превышать 500 символов'})
    
    class Meta:
        model = Reviews
        fields = ['text','category']

class PhotoAdminFrom(ModelForm):

    class Meta:
        model = Photo
        fields = ['name', 'image', 'category']
