from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название изображения')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')

    def __str__(self):
        return self.title
