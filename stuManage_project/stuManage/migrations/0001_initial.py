# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-08 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ad_number', models.CharField(blank=True, max_length=16, null=True)),
                ('ad_name', models.CharField(blank=True, max_length=20, null=True)),
                ('ad_password', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('d_number', models.CharField(blank=True, max_length=8, null=True)),
                ('d_position', models.CharField(blank=True, max_length=36, null=True)),
                ('d_dormtype', models.BigIntegerField(blank=True, null=True)),
                ('d_isempty', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'dormitory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DormType',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('d_type', models.CharField(blank=True, max_length=8, null=True)),
                ('d_price', models.IntegerField(blank=True, null=True)),
                ('d_addtime', models.DateTimeField(blank=True, null=True)),
                ('d_edittime', models.DateTimeField(blank=True, null=True)),
                ('d_editadmin', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dorm_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FeeType',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('f_type', models.CharField(blank=True, max_length=8, null=True)),
                ('f_price', models.IntegerField(blank=True, null=True)),
                ('f_addtime', models.DateTimeField(blank=True, null=True)),
                ('f_edittime', models.DateTimeField(blank=True, null=True)),
                ('f_editadmin', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fee_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('s_number', models.CharField(blank=True, max_length=16, null=True)),
                ('s_name', models.CharField(blank=True, max_length=20, null=True)),
                ('s_gender', models.IntegerField(blank=True, null=True)),
                ('s_age', models.IntegerField(blank=True, null=True)),
                ('s_intro', models.CharField(blank=True, max_length=200, null=True)),
                ('s_idnumber', models.CharField(blank=True, db_column='s_Idnumber', max_length=20, null=True)),
                ('s_address', models.CharField(blank=True, max_length=80, null=True)),
                ('s_phone', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'students',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StuDorm',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('stu_id', models.BigIntegerField(blank=True, null=True)),
                ('dorm_id', models.BigIntegerField(blank=True, null=True)),
                ('dorm_isuse', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'stu_dorm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StuFee',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('study_fee', models.BooleanField(default=False)),
                ('dinner_fee', models.BooleanField(default=False)),
                ('insurance_fee', models.BooleanField(default=False)),
                ('other_fee', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'stu_fee',
                'managed': False,
            },
        ),
    ]