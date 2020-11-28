from django.db import models
from storage.models import Storage
from products.models import Product,Unit
from contractors.models import Contractor
"""
Модели документов поступления
"""

DOCUMENT_TYPES = (
    (0, 'Документ'),
    (1, 'Отмена'),
)

ARRIVAL_TYPES = (
    (0, 'Поступление товаров'),
    (1, 'Возврат поставщику'),
    (2, 'Возврат от покупателя'),
    (3, 'Внутренее перемещение')
)


class ExpectedArrival(models.Model):
    """Модель ожидаемой приемки"""
    kis_number = models.CharField(max_length=64, null=True, verbose_name='Номер заявки')
    kis_date = models.DateTimeField(null=True, verbose_name='Дата заявки')
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата')
    type = models.PositiveSmallIntegerField(choices=ARRIVAL_TYPES, default=0)
    contractor = models.ForeignKey(to=Contractor, verbose_name='Контрагент', on_delete=models.CASCADE,
                                   null=True, )

    def __str__(self):
        return f"Arrival {self.id} of {self.contractor.name}"


    def add_entry(self, **kwargs):
        entry = self.entry.create(**kwargs)
        return entry


class ExpectedArrivalEntry(models.Model):
    """Строка ожидаемой приемки"""
    expected_arrival = models.ForeignKey(ExpectedArrival, verbose_name='Ожидаемая Приемка',
                                         on_delete=models.CASCADE, null=True, related_name='entry')
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField('Количество', default=0)

    def __str__(self):
        return f"Expected entry {self.expected_arrival.id} {self.product.name} {self.quantity}"


class Arrival(models.Model):
    """Модель документа прихода"""
    date = models.DateTimeField(auto_now_add=True, null=True)
    type = models.PositiveSmallIntegerField(choices=ARRIVAL_TYPES, default=0)
    expected_arrival = models.ForeignKey(ExpectedArrival, verbose_name='Ожидаемая Приемка',
                                         on_delete=models.CASCADE, null=True)


class ArrivalEntry(Storage):
    """Модель строки приемки"""
    arrival = models.ForeignKey(Arrival, verbose_name='Приемка', on_delete=models.CASCADE, null=True)
    document_type = models.PositiveSmallIntegerField('Тип', choices=DOCUMENT_TYPES, default=0)
