from django.db import models

"""
Модели контрагентов
"""

CONTRACTOR_TYPES = (
    ('Поставщик', 0),
    ('Покупатель', 1)
)

class Contractor(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    type = models.PositiveSmallIntegerField(choices=CONTRACTOR_TYPES, default=0)

    def __str__(self):
        return self.name