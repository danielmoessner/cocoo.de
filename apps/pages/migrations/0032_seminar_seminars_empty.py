# Generated by Django 3.2.3 on 2021-05-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_auto_20210517_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='seminars_empty',
            field=models.TextField(blank=True, verbose_name='Keine Seminare vorhanden'),
        ),
    ]