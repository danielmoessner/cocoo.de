# Generated by Django 3.1.6 on 2021-04-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0015_auto_20210411_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='members',
            field=models.ManyToManyField(related_name='certificates', to='team.Member', verbose_name='Teammitglieder'),
        ),
    ]
