from django.db import models
from storage.models import Storage
from products.models import Product,Unit
from contractors.models import Contractor
"""
Модели документов поступления
"""

DOCUMENT_TYPES = (
    ('document', 0),
    ('cancel', 1),
)

ARRIVAL_TYPES = (
    ('Поступление товаров', 0),
    ('Возврат поставщику', 1),
    ('Возврат от покупателя', 2),
    ('Внутренее перемещение', 3)
)

class ExpectedArrival(models.Model):
    """Модель ожидаемой приемки"""
    type = models.PositiveSmallIntegerField(choices=ARRIVAL_TYPES, default=0)
    contractor = models.ForeignKey(to=Contractor, verbose_name='Контрагент', on_delete=models.CASCADE,
                                   null=True, )

    def __str__(self):
        return f"Arrival {self.id} of {self.contractor.name}"

class ExpectedArrivalEntry(models.Model):
    """Строка ожидаемой приемки"""
    expected_arrival = models.ForeignKey(ExpectedArrival, verbose_name='Ожидаемая Приемка',
                                         on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField('Количество', default=0)

    def __str__(self):
        return f"Expected entry {self.expected_arrival.id} {self.product.name} {self.quantity}"

class Arrival(models.Model):
    """Модель документа прихода"""
    type = models.PositiveSmallIntegerField(choices=ARRIVAL_TYPES, default=0)

class ArrivalEntry(Storage):
    """Модель строки приемки"""
    arrival = models.ForeignKey(Arrival, verbose_name='Приемка', on_delete=models.CASCADE, null=True)
    document_type = models.PositiveSmallIntegerField('Тип', choices=DOCUMENT_TYPES, default=0)
