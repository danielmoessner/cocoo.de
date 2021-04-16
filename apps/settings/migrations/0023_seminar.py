# Generated by Django 3.1.6 on 2021-04-16 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0022_auto_20210401_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_pretitle', models.CharField(max_length=80, verbose_name='Inhalt Vortitel')),
                ('content_title', models.CharField(max_length=80, verbose_name='Inhalt Titel')),
                ('infos_title', models.CharField(max_length=80, verbose_name='Infos Titel')),
                ('infos_subtitle1', models.CharField(max_length=80, verbose_name='Infos Untertitel 1')),
                ('infos_subtitle2', models.CharField(max_length=80, verbose_name='Infos Untertitel 2')),
                ('infos_subtitle3', models.CharField(max_length=80, verbose_name='Infos Untertitel 3')),
                ('seminars_title', models.CharField(max_length=80, verbose_name='Seminare Titel')),
                ('form_title', models.CharField(max_length=80, verbose_name='Formular Titel')),
                ('form_text', models.CharField(max_length=140, verbose_name='Formular Text')),
                ('form_dataprotection', models.CharField(max_length=200, verbose_name='Formular Datenschutz Text')),
                ('form_requiredfields', models.CharField(max_length=200, verbose_name='Formular Muss Felder Text')),
                ('form_button', models.CharField(max_length=200, verbose_name='Formular Button')),
            ],
            options={
                'verbose_name': 'Seminar',
            },
        ),
    ]
