from django.db import models


class Abonement(models.Model):
    class Mark(models.TextChoices):
        JAN = "✔", "✔"
        FEB = "🞬", "🞬"
        
    title = models.CharField(max_length=50, verbose_name='Срок абонемента')
    
    mark_freeze = models.CharField(
        max_length=2,
        choices=Mark.choices,
        default=Mark.JAN,
        verbose_name='Есть ли заморозка?'
    )
    freeze = models.CharField(
        max_length=200,
        verbose_name='Кол-во дней заморозки'
    )
    
    mark_trainer = models.CharField(
        max_length=2,
        choices=Mark.choices,
        default=Mark.JAN,
        verbose_name='Есть ли спец тренеры?'
    )
    trainer = models.CharField(
        max_length=200,
        verbose_name='Кол-во спец тренеров'
    )
    
    mark_guest = models.CharField(
        max_length=2,
        choices=Mark.choices,
        default=Mark.JAN,
        verbose_name='Есть ли гостевые визитов?'
    )
    guest = models.CharField(
        max_length=200,
        verbose_name='Кол-во дней гостевых визитов'
    )
    time = models.CharField(max_length=150, verbose_name='Время посещения')
    price = models.CharField(
        max_length=20, verbose_name='Стоимость')
    special = models.BooleanField(verbose_name='Специальное предложение?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Абонемент',
        verbose_name_plural = 'Абонементы'
