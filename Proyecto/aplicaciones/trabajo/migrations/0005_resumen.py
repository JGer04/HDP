# Generated by Django 4.2.1 on 2023-05-31 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajo', '0004_remove_tablatipodiscapacidad_numero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='resumen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumen', models.TextField()),
            ],
        ),
    ]