# Generated by Django 3.1.5 on 2021-07-24 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20210723_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='tipo_persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='login.tipopersona', verbose_name='Cargo'),
        ),
    ]
