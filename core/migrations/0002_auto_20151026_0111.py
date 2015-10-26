# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='description',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='title',
        ),
        migrations.AddField(
            model_name='contact',
            name='email_Address',
            field=models.TextField(default=b'No email', max_length=300),
        ),
        migrations.AddField(
            model_name='contact',
            name='first_Name',
            field=models.TextField(default=b'No first name', max_length=300),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_Name',
            field=models.TextField(default=b'No last name', max_length=300),
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=b'No message', max_length=300),
        ),
    ]
