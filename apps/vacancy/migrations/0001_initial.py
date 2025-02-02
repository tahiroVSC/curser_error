# Generated by Django 5.0 on 2024-03-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='название')),
                ('title_ky', models.CharField(max_length=255, null=True, verbose_name='название')),
                ('desc', models.TextField(verbose_name='описание')),
                ('desc_ru', models.TextField(null=True, verbose_name='описание')),
                ('desc_ky', models.TextField(null=True, verbose_name='описание')),
                ('salary', models.CharField(max_length=255, verbose_name='зарплата')),
            ],
            options={
                'verbose_name': ('Вакансия',),
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
