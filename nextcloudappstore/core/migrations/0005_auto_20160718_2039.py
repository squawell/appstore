# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160705_2119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='database',
            options={'ordering': ['name'], 'verbose_name': 'Database', 'verbose_name_plural': 'Databases'},
        ),
        migrations.AlterModelOptions(
            name='phpextension',
            options={'ordering': ['id'], 'verbose_name': 'PHP Extension', 'verbose_name_plural': 'PHP Extensions'},
        ),
        migrations.AlterModelOptions(
            name='shellcommand',
            options={'ordering': ['name'], 'verbose_name': 'Shell Command', 'verbose_name_plural': 'Shell Commands'},
        ),
    ]