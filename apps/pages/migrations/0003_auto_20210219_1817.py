# Generated by Django 3.1.6 on 2021-02-19 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_dataprotection'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataprotection',
            name='heading',
            field=models.CharField(default='Datenschutz', max_length=200, verbose_name='Überschrift'),
        ),
        migrations.AddField(
            model_name='imprint',
            name='heading',
            field=models.CharField(default='Impressum', max_length=200, verbose_name='Überschrift'),
        ),
    ]
