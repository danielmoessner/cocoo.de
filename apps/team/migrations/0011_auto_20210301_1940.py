# Generated by Django 3.1.6 on 2021-03-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_member_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='slug',
            field=models.SlugField(help_text='Erscheint in der URL. Zum Beispiel: cocoo.de/team/max-mustermann/.', unique=True, verbose_name='Slug'),
        ),
    ]