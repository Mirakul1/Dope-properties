# Generated by Django 2.2.8 on 2019-12-09 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listing_id',
            new_name='property_id',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='listing',
        ),
        migrations.AddField(
            model_name='contact',
            name='prop',
            field=models.CharField(default=0, max_length=200, verbose_name='property'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 9, 1, 11, 17, 528885)),
        ),
    ]
