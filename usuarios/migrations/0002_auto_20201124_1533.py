# Generated by Django 3.1.3 on 2020-11-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={},
        ),
        migrations.AlterModelManagers(
            name='usuarios',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
