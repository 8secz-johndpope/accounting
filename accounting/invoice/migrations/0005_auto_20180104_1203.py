# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-04 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20180104_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinvoice',
            name='pdf_path',
            field=models.URLField(blank=True, help_text='The absolute URL that can be used to retrieve the invoice PDF.', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='pdf_path',
            field=models.URLField(blank=True, help_text='The absolute URL that can be used to retrieve the invoice PDF.', max_length=300, null=True),
        ),
    ]