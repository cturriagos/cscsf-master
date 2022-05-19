# Generated by Django 3.1.5 on 2021-07-31 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representantetecnico', '0015_auto_20210721_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compraspublicas',
            name='hora_llegada_bodega',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='Hora llegada a bodega'),
        ),
        migrations.AlterField(
            model_name='compraspublicas',
            name='llegada_bodega',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha llegada a bodega'),
        ),
    ]