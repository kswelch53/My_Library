# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-25 05:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mylibrary1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('adds_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='mylibrary1.User')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booklink', to='mylibrary2.Book')),
                ('user_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userlink', to='mylibrary1.User')),
            ],
        ),
    ]
