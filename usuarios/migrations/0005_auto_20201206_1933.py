# Generated by Django 3.1.3 on 2020-12-07 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuarios_monto_pagar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='monto_pagar',
            field=models.IntegerField(default=0),
        ),
    ]
