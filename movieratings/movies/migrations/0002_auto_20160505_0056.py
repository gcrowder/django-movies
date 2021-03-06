# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Ratings',
            new_name='Rating',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='ratings',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='ratings',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.DeleteModel(
            name='Rater',
        ),
    ]
