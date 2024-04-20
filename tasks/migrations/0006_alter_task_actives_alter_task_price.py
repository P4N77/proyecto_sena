# Generated by Django 5.0.3 on 2024-04-20 17:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_task_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='actives',
            field=models.CharField(choices=[('d', 'Disponible'), ('n', 'No Disponible')], max_length=1, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='task',
            name='price',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='valor por unidad'),
        ),
    ]
