# Generated by Django 3.1.5 on 2021-04-04 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0002_auto_20210403_1305'),
        ('representantetecnico', '0002_auto_20210403_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='bodega',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bodega.bodega', verbose_name='Bodega'),
        ),
    ]