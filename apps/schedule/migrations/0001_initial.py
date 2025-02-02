# Generated by Django 5.0 on 2024-03-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_time', models.CharField(max_length=100, verbose_name='Время работы по будням')),
                ('work_time_ru', models.CharField(max_length=100, null=True, verbose_name='Время работы по будням')),
                ('work_time_ky', models.CharField(max_length=100, null=True, verbose_name='Время работы по будням')),
                ('holiday_work_time', models.CharField(max_length=100, verbose_name='Время работы в выходные и праздничные дни')),
                ('holiday_work_time_ru', models.CharField(max_length=100, null=True, verbose_name='Время работы в выходные и праздничные дни')),
                ('holiday_work_time_ky', models.CharField(max_length=100, null=True, verbose_name='Время работы в выходные и праздничные дни')),
            ],
            options={
                'verbose_name': 'График работы',
                'verbose_name_plural': 'График работы',
            },
        ),
    ]
