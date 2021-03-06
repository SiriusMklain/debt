# Generated by Django 3.2.6 on 2021-08-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='investpost',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterField(
            model_name='investpost',
            name='statusProject',
            field=models.CharField(choices=[('active', 'Активный'), ('completed', 'Завершенный')], max_length=250, verbose_name='Статус проекта'),
        ),
    ]
