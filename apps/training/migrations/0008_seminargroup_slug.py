# Generated by Django 3.1.6 on 2021-02-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0007_auto_20210224_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminargroup',
            name='slug',
            field=models.SlugField(default='', verbose_name='Slug'),
            preserve_default=False,
        ),
    ]