# Generated by Django 4.2.4 on 2023-08-23 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_remove_genres_name_alter_borrowing_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='borrowing',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 22, 14, 16, 13, 660470, tzinfo=datetime.timezone.utc)),
        ),
    ]