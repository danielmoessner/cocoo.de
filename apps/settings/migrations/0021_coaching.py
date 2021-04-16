# Generated by Django 3.1.6 on 2021-04-01 13:49

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0020_auto_20210401_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField(verbose_name='Inhalt')),
            ],
            options={
                'verbose_name': 'Coaching',
            },
        ),
    ]
