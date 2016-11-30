# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 22:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedditJson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_fetched', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'redditjson',
            },
        ),
        migrations.CreateModel(
            name='RedditPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subreddit', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'redditpost',
            },
        ),
    ]