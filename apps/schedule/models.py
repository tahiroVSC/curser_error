from django.db import models


class Schedule(models.Model):
    work_time = models.CharField(verbose_name="Время работы по будням", max_length=100)
    holiday_work_time = models.CharField(verbose_name="Время работы в выходные и праздничные дни", max_length=100)

    def __str__(self):
        return self.work_time

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'График работы'
