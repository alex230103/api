# Generated by Django 3.1.3 on 2020-11-20 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arrivals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrivalentry',
            name='posted',
        ),
    ]
