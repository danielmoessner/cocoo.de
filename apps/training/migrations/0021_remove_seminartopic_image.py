# Generated by Django 3.1.6 on 2021-04-30 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0020_auto_20210423_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seminartopic',
            name='image',
        ),
    ]
