# Generated by Django 3.1.6 on 2021-02-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20210219_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seminarexecution',
            options={'ordering': ['title'], 'verbose_name': 'Seminardurchführung', 'verbose_name_plural': 'Seminardurchführungen'},
        ),
        migrations.AlterField(
            model_name='seminarexecution',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='seminargroup',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='seminartopic',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
