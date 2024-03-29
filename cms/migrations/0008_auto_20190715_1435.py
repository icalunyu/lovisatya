# Generated by Django 2.2.3 on 2019-07-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20190714_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guest',
            field=models.CharField(choices=[('', 'Will you bring plus one?'), ('notalone', 'Yes, I Will.'), ('alone', 'No. I`m coming alone')], max_length=255),
        ),
    ]
