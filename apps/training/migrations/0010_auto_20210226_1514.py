# Generated by Django 3.1.6 on 2021-02-26 14:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0009_auto_20210226_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminartopic',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Beschreibung'),
        ),
    ]