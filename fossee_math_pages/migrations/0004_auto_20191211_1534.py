# Generated by Django 2.2.8 on 2019-12-11 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fossee_math_pages', '0003_auto_20191211_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 15, 34, 11, 945751)),
        ),
    ]
