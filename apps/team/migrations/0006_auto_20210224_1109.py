# Generated by Django 3.1.6 on 2021-02-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20210219_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Entwurf'),
        ),
        migrations.AlterField(
            model_name='member',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Entwurf'),
        ),
    ]