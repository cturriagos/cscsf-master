# Generated by Django 3.1.5 on 2021-08-22 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('representantetecnico', '0024_auto_20210815_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicituddetalle',
            name='cantidad_consumida',
        ),
    ]
