# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytranslation',
            name='description',
            field=models.TextField(default='This is a default description', help_text='Will be rendered as Markdown', verbose_name='Description'),
            preserve_default=False,
        ),
    ]
