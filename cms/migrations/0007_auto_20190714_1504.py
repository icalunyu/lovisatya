# Generated by Django 2.2.3 on 2019-07-14 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rsvp',
            old_name='code',
            new_name='keypass',
        ),
    ]