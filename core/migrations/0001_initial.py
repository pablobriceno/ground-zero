# Generated by Django 3.2.4 on 2021-07-06 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arte',
            fields=[
                ('idArte', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Arte')),
                ('nombreArte', models.CharField(max_length=50, verbose_name='Nombre del arte')),
                ('descripcionArte', models.CharField(max_length=255, verbose_name='Descripcion de el arte')),
                ('historiaArte', models.CharField(max_length=255, verbose_name='Historia sobre el arte')),
                ('tecnicaUsada', models.CharField(max_length=60, verbose_name='Tecnica usada en el arte')),
                ('destacado', models.BooleanField(default=False, verbose_name='El arte es destacado o no')),
                ('precio', models.IntegerField(verbose_name='Precio del arte')),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('idArtista', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Artista')),
                ('pNombre', models.CharField(max_length=50, verbose_name='Primer nombre del artista')),
                ('sNombre', models.CharField(max_length=50, null=True, verbose_name='Segundo nombre del artista')),
                ('apPaterno', models.CharField(max_length=50, verbose_name='Apellido paterno del artista')),
                ('apMaterno', models.CharField(max_length=50, null=True, verbose_name='Apellido materno del artista')),
                ('email', models.CharField(max_length=255, verbose_name='Email del artista')),
                ('clave', models.CharField(max_length=255, verbose_name='Contraseña del artista')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('idImagen', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Imagen')),
                ('url', models.CharField(max_length=255, verbose_name='URL de la imagen')),
                ('idArte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.arte')),
            ],
        ),
        migrations.AddField(
            model_name='arte',
            name='idArtista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artista'),
        ),
    ]