# Generated by Django 3.1.5 on 2021-07-21 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20210720_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='tipo_persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='login.tipopersona', verbose_name='Tipo de persona'),
        ),
        migrations.AlterField(
            model_name='user',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='login.persona', verbose_name='Persona'),
        ),
    ]
