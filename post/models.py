from django.db import models

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
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title} hhh'
    
