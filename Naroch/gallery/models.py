from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    OUTSIDE = 'улица'
    AREA = 'участок'
    FIRST_HOUSE = 'первый_дом'
    SECOND_HOUSE = 'второй_дом'
    BATH_HOUSE = 'баня'

    CHOICE_GROUP = { # Категории
    (OUTSIDE, 'улица'),
    (AREA, 'участок'),
    (FIRST_HOUSE, 'первый_дом'),
    (SECOND_HOUSE, 'второй_дом'),
    (BATH_HOUSE, 'баня')
    }

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=15, choices= CHOICE_GROUP, default=OUTSIDE) # Выбераем из нашей группы по умолчанию OTSIDE
    image = models.ImageField(upload_to = "images/")

    def get_absolute_url(self):
        return f'/admin_for_staff/gallery_moderation'
    
    class Meta():
        verbose_name = "Фото"
        verbose_name_plural = "Фото"