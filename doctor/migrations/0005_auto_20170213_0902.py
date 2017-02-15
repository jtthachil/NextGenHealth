# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-13 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doc_image',
            field=models.ImageField(upload_to='/images/doctors'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='p_image',
            field=models.ImageField(upload_to='/images/patients'),
        ),
    ]