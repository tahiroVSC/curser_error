from django.db import models
from ckeditor.fields import RichTextField


class Vacancy(models.Model):

    title = models.CharField(
        verbose_name='название',
        max_length=255
    )
    desc =RichTextField(
        verbose_name='описание'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия',
        verbose_name_plural = 'Вакансии'
