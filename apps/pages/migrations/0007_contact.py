# Generated by Django 3.1.6 on 2021-03-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210318_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_heading', models.CharField(max_length=80, verbose_name='Kontaktüberschrift')),
                ('contact_emailphone', models.CharField(max_length=50, verbose_name='E-Mail und Telefon Überschrift')),
                ('contact_address', models.CharField(max_length=50, verbose_name='Adresse Überschrift')),
                ('form_heading', models.CharField(max_length=80, verbose_name='Formularüberschrift')),
                ('form_buttontext', models.CharField(max_length=100, verbose_name='Formular Button Text')),
                ('form_dataprotectiontext', models.CharField(max_length=200, verbose_name='Formular Datenschutz Text')),
            ],
            options={
                'verbose_name': 'Kontakt',
            },
        ),
    ]
