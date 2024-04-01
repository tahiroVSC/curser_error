from django.db import models
from ckeditor.fields import RichTextField


class Review(models.Model):
    photo = models.ImageField(
        verbose_name= "Фотография",
        upload_to= "review/"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    jobtitle = models.CharField(
        max_length = 255,
        verbose_name = "Должность"
    )
    description = RichTextField(
        verbose_name="Отзыв"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
