# Generated by Django 4.2.2 on 2023-06-21 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='post',
            new_name='blog',
        ),
    ]
