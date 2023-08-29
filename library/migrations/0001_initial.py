# Generated by Django 4.2.4 on 2023-08-29 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('availability', models.BooleanField(default=True)),
                ('author', models.TextField()),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'books',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('borrowing_id', models.AutoField(primary_key=True, serialize=False)),
                ('details', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default=datetime.datetime(2023, 9, 28, 20, 23, 34, 400584, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'db_table': 'borrowings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'genres',
                'managed': False,
            },
        ),
    ]
