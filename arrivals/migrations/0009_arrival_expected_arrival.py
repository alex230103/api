# Generated by Django 3.1.3 on 2020-11-21 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrivals', '0008_auto_20201120_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrival',
            name='expected_arrival',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='arrivals.expectedarrival', verbose_name='Ожидаемая Приемка'),
        ),
    ]