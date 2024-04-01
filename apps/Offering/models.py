from django.db import models


class Icons(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название иконки"
    )
    icon = models.ImageField(
        verbose_name = 'Иконка',
        upload_to='offering_icon/',
    )
    
    class Meta:
        verbose_name='Иконка'
        verbose_name_plural='Иконки'
    
    def __str__(self):
        return self.name


class Offering(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    price = models.CharField(
        max_length=255,
        verbose_name="Цена", 
        null = True, blank=True 
    ) 
    image = models.ForeignKey(
        Icons,
        on_delete=models.CASCADE,
        verbose_name='картинки услуг'
        )
    hide = models.BooleanField(
        verbose_name='Cкрыть'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
