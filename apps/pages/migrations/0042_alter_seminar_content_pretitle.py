# Generated by Django 3.2.3 on 2021-06-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0041_auto_20210617_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminar',
            name='content_pretitle',
            field=models.CharField(blank=True, max_length=80, verbose_name='Inhalt // Vortitel'),
        ),
    ]
