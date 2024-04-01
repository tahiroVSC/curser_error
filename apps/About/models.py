from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    desc = RichTextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='about/')
    
    def __str__(self):
        return 'О нас'

    class Meta:
        verbose_name = 'О нас',
        verbose_name_plural = 'О нас'
