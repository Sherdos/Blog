from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    
    title = models.CharField(
        verbose_name='название',
        max_length=255
        )

    desciption = models.TextField(
        verbose_name='Описание'
    )
    
    image = models.ImageField(
        verbose_name='фото',
        upload_to='posts/image/'
    )
    
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_post',
        verbose_name='пользователь')
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title} hhh'
    
