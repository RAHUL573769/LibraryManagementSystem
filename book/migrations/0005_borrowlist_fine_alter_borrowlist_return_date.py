# Generated by Django 4.2.3 on 2023-09-02 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_borrowlist_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowlist',
            name='fine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='borrowlist',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 16, 32, 11, 536728)),
        ),
    ]
