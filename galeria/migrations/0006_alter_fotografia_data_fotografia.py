# Generated by Django 5.1.6 on 2025-02-13 22:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_fotografia_data_fotografia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 13, 19, 46, 32, 906366)),
        ),
    ]
