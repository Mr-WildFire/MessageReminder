# Generated by Django 4.2.3 on 2023-07-21 02:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_alert', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message_title',
        ),
        migrations.AddField(
            model_name='message',
            name='setup_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 7, 21, 10, 3, 2, 53424)),
            preserve_default=False,
        ),
    ]