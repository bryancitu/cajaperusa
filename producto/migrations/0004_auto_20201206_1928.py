# Generated by Django 3.1.3 on 2020-12-07 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_datoscita_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoscita',
            name='fecha_cita',
            field=models.DateTimeField(verbose_name='Fecha de la Cita'),
        ),
    ]