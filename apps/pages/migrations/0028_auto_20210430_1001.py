# Generated by Django 3.1.6 on 2021-04-30 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_delete_general'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coaching',
            name='header_image',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='header_image',
        ),
        migrations.RemoveField(
            model_name='index',
            name='header_image',
        ),
        migrations.RemoveField(
            model_name='seminars',
            name='header_image',
        ),
        migrations.RemoveField(
            model_name='team',
            name='header_image',
        ),
    ]
