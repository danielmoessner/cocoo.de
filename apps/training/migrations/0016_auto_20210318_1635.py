# Generated by Django 3.1.6 on 2021-03-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0015_remove_seminartopic_trainers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminarexecution',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Plätze verfügbar'), ('ALMOST_FULL', 'Wenige Plätze verfügbar'), ('FULL', 'Ausgebucht')], max_length=50, verbose_name='Buchungsstatus'),
        ),
    ]
