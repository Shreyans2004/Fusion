# Generated by Django 3.1.5 on 2024-04-19 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_procedures', '0002_auto_20240419_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_allocations',
            name='start_date',
            field=models.DateField(default=datetime.date(2024, 4, 19)),
        ),
    ]
