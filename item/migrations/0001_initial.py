# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_price', models.FloatField()),
                ('posted_by', models.CharField(max_length=100)),
                ('number_of_items', models.IntegerField()),
                ('item_categories', models.CharField(max_length=100)),
                ('item_description', models.CharField(max_length=500)),
                ('item_rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('comment', models.CharField(max_length=500)),
                ('item', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='item.Item')),
            ],
        ),
    ]
