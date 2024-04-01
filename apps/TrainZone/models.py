from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class TrainZone(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    section = models.CharField(max_length=200, default="trainzone")


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Тренировочная зона',
        verbose_name_plural = 'Тренировочные зоны'


class TrainZoneImage(models.Model):
    trainzone= models.ForeignKey(TrainZone, default=None, on_delete=models.CASCADE, related_name='images')
    images = models.FileField(upload_to='media/')

    def __str__(self):
        return self.trainzone.title
