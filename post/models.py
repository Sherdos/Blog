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
        return f'{self.title}'
    

class Comment(models.Model):
    text = models.TextField('текст')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='com_user', verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='com_post', verbose_name='Пост' )
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
     
    def __str__(self):
        return f'{self.user} '   
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user', verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post', verbose_name='Пост' )
    
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
     
    def __str__(self):
        return f'{self.user} '   
    
    

class Review(models.Model):
    text = models.TextField('текст')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rev_user', verbose_name='Пользователь')
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
     
    def __str__(self):
        return f'{self.user} ' 