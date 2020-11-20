# Generated by Django 3.1.3 on 2020-11-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrivals', '0004_auto_20201120_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrival',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[('Поступление товаров', 0), ('Возврат поставщику', 1), ('Возврат от покупателя', 2), ('Внутренее перемещение', 3)], default=0),
        ),
        migrations.AddField(
            model_name='expectedarrival',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[('Поступление товаров', 0), ('Возврат поставщику', 1), ('Возврат от покупателя', 2), ('Внутренее перемещение', 3)], default=0),
        ),
    ]
