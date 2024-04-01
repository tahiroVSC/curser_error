from django.db import models


class Contact(models.Model):
    first_number = models.CharField(max_length=16, verbose_name="Номер телефона")
    second_number = models.CharField(max_length=16, verbose_name="Второй номер")
    email = models.EmailField(verbose_name="Введите почту", blank=True, null=True)
    address = models.CharField(max_length=150, verbose_name="Адресс")
    links = models.URLField(verbose_name="Введите ссылку", blank=True, null=True)

    def __str__(self):
        return self.first_number

    class Meta:
        verbose_name = 'Контакт',
        verbose_name_plural = 'Контакты'
