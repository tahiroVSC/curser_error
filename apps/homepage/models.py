from django.db import models


class HomePage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=200, verbose_name="Подзаголовок")
    photo = models.FileField(upload_to='homepage/', verbose_name="Фото")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Стартовый блок"
        verbose_name_plural = "Стартовый блок"
