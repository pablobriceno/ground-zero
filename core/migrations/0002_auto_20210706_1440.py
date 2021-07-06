# Generated by Django 3.2.4 on 2021-07-06 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arte',
            name='fechaSubida',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de subida del arte'),
        ),
        migrations.AlterField(
            model_name='arte',
            name='precio',
            field=models.IntegerField(null=True, verbose_name='Precio del arte'),
        ),
    ]