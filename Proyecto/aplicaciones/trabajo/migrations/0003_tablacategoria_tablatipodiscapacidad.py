# Generated by Django 4.2.1 on 2023-05-31 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajo', '0002_rename_mujer_tablaencuestarural_mujer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tablaCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
                ('hombre', models.IntegerField()),
                ('mujer', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Tabla Categoria',
            },
        ),
        migrations.CreateModel(
            name='tablaTipoDiscapacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discapacidad', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('porcentaje', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Tabla Tipo Discapacidad',
            },
        ),
    ]
