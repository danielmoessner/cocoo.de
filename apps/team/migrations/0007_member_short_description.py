# Generated by Django 3.1.6 on 2021-02-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_auto_20210224_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='short_description',
            field=models.TextField(default='', verbose_name='Kurzbeschreibung'),
            preserve_default=False,
        ),
    ]