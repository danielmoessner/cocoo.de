# Generated by Django 3.1.6 on 2021-04-16 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0018_seminarexecution_show_on_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seminarexecution',
            options={'ordering': ['-start_date'], 'verbose_name': 'Seminardurchführung', 'verbose_name_plural': 'Seminardurchführungen'},
        ),
    ]
