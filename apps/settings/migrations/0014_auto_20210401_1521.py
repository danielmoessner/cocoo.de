# Generated by Django 3.1.6 on 2021-04-01 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_index_seminartopiclist_team'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SeminarTopicList',
            new_name='Seminars',
        ),
    ]
