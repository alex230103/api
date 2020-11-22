from django.db import models
"""
Основные модели продуктов
"""


class Unit(models.Model):
    """Модель еденицы хранения"""
    product = models.ForeignKey('Product', verbose_name='Продукт', on_delete=models.CASCADE, related_name='units')
    name = models.CharField('Название', max_length=64)
    ratio = models.PositiveSmallIntegerField('Коэфициент', default=1)

    def __str__(self):
        return f"Unit {self.name} ({self.ratio})"

    class Meta:
        """ Проверка уникальности по коэффициенту"""
        unique_together = ['product', 'ratio']


class Product(models.Model):
    """ Модель товара """
    name = models.CharField("Название", max_length=64, unique=True)
    base_unit = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name='base_unit', null=True)

    @classmethod
    def create_product(cls, **kwargs):
        """Метод для создания продукта, авто создание базовой единицы хранения"""
        product = cls.objects.create(**kwargs)
        unit = Unit.objects.create(name='base', product=product)
        product.base_unit = unit
        product.save()
        return product

    def __str__(self):
        return f"Product {self.name}"
