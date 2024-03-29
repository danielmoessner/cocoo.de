# Generated by Django 3.1.6 on 2021-04-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_coaching'),
    ]

    operations = [
        migrations.AddField(
            model_name='coaching',
            name='header_heading',
            field=models.CharField(default='', max_length=60, verbose_name='Header Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coaching',
            name='header_image',
            field=models.ImageField(default='', upload_to='team/', verbose_name='Header Bild'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coaching',
            name='header_text',
            field=models.CharField(default='', max_length=200, verbose_name='Header Text'),
            preserve_default=False,
        ),
    ]
