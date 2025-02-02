# Generated by Django 5.0 on 2024-03-28 17:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0002_alter_review_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='review',
            name='description_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='review',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Отзыв'),
        ),
    ]
