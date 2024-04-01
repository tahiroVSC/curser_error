from django.db import models
from ckeditor.fields import RichTextField


class Type_of_trainer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название вида тренировки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = " Вид тренера"
        verbose_name_plural = "Виды  тренеров"


# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=250, verbose_name="Фамилия Имя")
    position = models.CharField(max_length=250, verbose_name="Должность")
    photo = models.ImageField(upload_to='trainer/', verbose_name="Изображение",  default='/trainer/default.jpg')
    description = RichTextField(verbose_name="Описание")
    type_of_trainer = models.ForeignKey(Type_of_trainer, on_delete=models.PROTECT, verbose_name="Зал")
    section = models.CharField(max_length=200, default="trainer")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"
