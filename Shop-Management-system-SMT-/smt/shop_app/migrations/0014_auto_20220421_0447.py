# Generated by Django 3.2.12 on 2022-04-21 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0013_alter_assigncleanerd_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigncleanerd',
            name='date',
            field=models.DateTimeField(default=datetime.date(2022, 4, 21), null=True),
        ),
        migrations.AlterField(
            model_name='assigncleanergroup',
            name='date',
            field=models.DateField(default=datetime.date(2022, 4, 21)),
        ),
        migrations.AlterField(
            model_name='cleanerrecord',
            name='date',
            field=models.DateField(default=datetime.date(2022, 4, 21)),
        ),
    ]