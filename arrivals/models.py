from django.db import models
from storage.models import Storage
from products.models import Product,Unit

"""
Модели документов поступления
"""

DOCUMENT_TYPES = (
    ('document', 0),
    ('cancel', 1),
)

class ExpectedArrival(models.Model):
    """Модель ожидаемой приемки"""
    ...

class ExpectedArrivalEntry(models.Model):
    """Строка ожидаемой приемки"""
    ...

class ArrivalEntry(Storage):
    """Модель строки приемки"""
    document_type = models.PositiveSmallIntegerField('Тип', choices=DOCUMENT_TYPES, default=0)
