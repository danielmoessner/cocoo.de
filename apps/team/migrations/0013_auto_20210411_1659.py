# Generated by Django 3.1.6 on 2021-04-11 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0012_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certification',
            options={'ordering': ['name'], 'verbose_name': 'Zertifikat', 'verbose_name_plural': 'Zertifikate'},
        ),
        migrations.RemoveField(
            model_name='certification',
            name='member',
        ),
    ]