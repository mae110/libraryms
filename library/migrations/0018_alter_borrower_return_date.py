# Generated by Django 3.2.9 on 2021-11-18 00:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_alter_borrower_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 2, 3, 32, 771697)),
        ),
    ]
