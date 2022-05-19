# Generated by Django 3.1.5 on 2021-07-27 16:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20210724_1748'),
        ('tecnicolaboratorio', '0003_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 27, 11, 31, 21, 935458), null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 27, 11, 31, 21, 935458), null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='responsable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='login.persona', verbose_name='Responsable'),
        ),
    ]