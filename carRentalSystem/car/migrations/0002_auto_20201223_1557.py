# Generated by Django 3.1.4 on 2020-12-23 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[ a-zA-Z]*$', 'Only alphabets are allowed.')]),
        ),
    ]