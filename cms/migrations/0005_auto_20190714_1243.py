# Generated by Django 2.2.3 on 2019-07-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_rsvp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
