# Generated by Django 4.2.1 on 2023-06-03 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajo', '0006_analisis_alter_resumen_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analisis',
            name='resumen',
        ),
        migrations.AddField(
            model_name='analisis',
            name='analisis',
            field=models.TextField(default=''),
        ),
    ]