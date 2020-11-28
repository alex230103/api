from django.db import models

"""
Модели контрагентов
"""

CONTRACTOR_TYPES = (
    (0, 'Поставщик'),
    (1, 'Покупатель')
)


class Contractor(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    type = models.PositiveSmallIntegerField(choices=CONTRACTOR_TYPES, default=0)

    def __str__(self):
        return self.name