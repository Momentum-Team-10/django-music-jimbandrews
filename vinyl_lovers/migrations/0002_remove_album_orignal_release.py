# Generated by Django 3.2.9 on 2021-11-06 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl_lovers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='orignal_release',
        ),
    ]
