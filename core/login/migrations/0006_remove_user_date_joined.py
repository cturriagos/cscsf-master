# Generated by Django 3.1.5 on 2021-07-23 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210721_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
    ]
