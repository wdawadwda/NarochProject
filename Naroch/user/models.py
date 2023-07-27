from django.db import models
from django.contrib.auth.models import User

class Reviews(models.Model):
    verified = 'верифицирован'
    not_verified = 'не верифицирован'

    CHOICE_GROUP = {
    (verified, 'верифицирован'),
    (not_verified, 'не верифицирован')
    }

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Текст комментария", max_length=500)
    reviews_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=35, choices = CHOICE_GROUP, default = not_verified)

    def __str__(self):
        return f'Автор{self.username}, Комментарий {self.text}, Дата публикации {self.reviews_date}'

    def get_absolute_url(self):
        return f'/admin_for_staff/comment_moderation/{self.id}'

    class Meta():
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
