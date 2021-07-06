# Generated by Django 3.2.4 on 2021-07-06 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210706_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='arte',
            name='idCategoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.categoria', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='arte',
            name='idArtista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artista', verbose_name='Artista'),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='idArte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.arte', verbose_name='Arte'),
        ),
    ]