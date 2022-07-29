# Generated by Django 3.2.12 on 2022-04-14 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('smt_app', '0007_auto_20220414_0913'),
        ('shop_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssistanceSupervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smt_app.city')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('city', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='smt_app.city')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smt_app.city')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.manager')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor', to=settings.AUTH_USER_MODEL)),
                ('zone', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='smt_app.zone')),
            ],
        ),
        migrations.CreateModel(
            name='ShopOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('dob', models.CharField(max_length=30, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('ass_supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.assistancesupervisor')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smt_app.city')),
                ('cleaner_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop_app.cleanergroup')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cleaner', to=settings.AUTH_USER_MODEL)),
                ('zone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smt_app.zone')),
            ],
        ),
        migrations.AddField(
            model_name='assistancesupervisor',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.manager'),
        ),
        migrations.AddField(
            model_name='assistancesupervisor',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.supervisor'),
        ),
        migrations.AddField(
            model_name='assistancesupervisor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ass_supervisor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assistancesupervisor',
            name='zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smt_app.zone'),
        ),
    ]
