# Generated by Django 3.1.6 on 2021-03-04 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0014_auto_20210302_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seminartopic',
            name='trainers',
        ),
    ]
