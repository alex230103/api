from django.db import models
from polymorphic.models import PolymorphicModel
from products.models import Product, Unit


class Storage(PolymorphicModel):
    """Модель остатков"""
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    unit = models.ForeignKey(to=Unit, verbose_name='Единица хранения', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField('Количество', default=0)

