# Generated by Django 3.1.3 on 2020-12-07 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuarios_codregistro'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='monto_pagar',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]