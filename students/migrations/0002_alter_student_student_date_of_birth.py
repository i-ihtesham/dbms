# Generated by Django 4.0 on 2021-12-15 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_date_of_birth',
            field=models.DateField(default=datetime.date(2021, 12, 15)),
        ),
    ]
