# Generated by Django 3.1.6 on 2021-02-19 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Training',
        ),
    ]