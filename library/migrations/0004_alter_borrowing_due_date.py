# Generated by Django 4.2.4 on 2023-08-22 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_admin_id_remove_book_author_remove_book_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 21, 17, 57, 2, 766457, tzinfo=datetime.timezone.utc)),
        ),
    ]
