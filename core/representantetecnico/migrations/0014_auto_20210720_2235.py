# Generated by Django 3.1.5 on 2021-07-21 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representantetecnico', '0013_auto_20210416_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desgloseinfomemensualdetalle',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='informemensual/sustancias/desglose/%Y/%m/%d'),
        ),
    ]