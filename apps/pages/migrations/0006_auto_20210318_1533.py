# Generated by Django 3.1.6 on 2021-03-18 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_general'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='address_city',
            field=models.CharField(default='', max_length=100, verbose_name='Adresse Stadt'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='general',
            name='address_street',
            field=models.CharField(default='', max_length=100, verbose_name='Adresse Straße'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='general',
            name='email',
            field=models.CharField(default='', max_length=100, verbose_name='E-Mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='general',
            name='phone',
            field=models.CharField(default='', max_length=100, verbose_name='Telefon'),
            preserve_default=False,
        ),
    ]
