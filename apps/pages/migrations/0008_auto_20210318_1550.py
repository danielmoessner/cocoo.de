# Generated by Django 3.1.6 on 2021-03-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='header_heading',
            field=models.CharField(default='', max_length=60, verbose_name='Header Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='header_text',
            field=models.CharField(default='', max_length=100, verbose_name='Header Text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_heading',
            field=models.CharField(max_length=80, verbose_name='Kontakt Überschrift'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='form_heading',
            field=models.CharField(max_length=80, verbose_name='Formular Überschrift'),
        ),
    ]
