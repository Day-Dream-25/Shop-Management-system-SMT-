# Generated by Django 3.2.12 on 2022-04-20 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0010_assigncleanerd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigncleanerd',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_app.shopdetail'),
        ),
    ]
