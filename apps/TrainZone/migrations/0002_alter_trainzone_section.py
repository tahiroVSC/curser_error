# Generated by Django 5.0 on 2024-03-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrainZone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainzone',
            name='section',
            field=models.CharField(default='trainzone', max_length=200),
        ),
    ]
