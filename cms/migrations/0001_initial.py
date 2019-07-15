# Generated by Django 2.2.3 on 2019-07-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('guest', models.IntegerField()),
                ('attending', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
