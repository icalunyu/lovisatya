# Generated by Django 2.2.3 on 2019-07-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='attending',
            field=models.CharField(choices=[('all', 'All'), ('reception', 'Reception'), ('party', 'Dinner & Party')], max_length=255),
        ),
    ]