# Generated by Django 2.2.8 on 2019-12-05 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20191205_1118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterField(
            model_name='property',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 5, 11, 21, 44, 849421)),
        ),
    ]
