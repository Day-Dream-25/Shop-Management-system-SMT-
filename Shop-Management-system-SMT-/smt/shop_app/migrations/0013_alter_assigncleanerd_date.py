# Generated by Django 3.2.12 on 2022-04-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0012_alter_assigncleanerd_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigncleanerd',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
