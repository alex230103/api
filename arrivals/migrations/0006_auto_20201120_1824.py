# Generated by Django 3.1.3 on 2020-11-20 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0001_initial'),
        ('products', '0001_initial'),
        ('arrivals', '0005_auto_20201120_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='expectedarrival',
            name='contractor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contractors.contractor', verbose_name='Контрагент'),
        ),
        migrations.AddField(
            model_name='expectedarrivalentry',
            name='expected_arrival',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='arrivals.expectedarrival', verbose_name='Ожидаемая Приемка'),
        ),
        migrations.AddField(
            model_name='expectedarrivalentry',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='expectedarrivalentry',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество'),
        ),
    ]