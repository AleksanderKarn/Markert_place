from datetime import datetime

from django.db import models

from contacts.models import Contact

NULLABLE = {'blank': True, 'null': True}


class Provider(models.Model):
    FACTORY = 'Factory'
    MARKET = 'Market'
    BUSINESSMAN = 'Businessman'

    TYPE_LINK = (
        ('Factory', 'завод'),
        ('Market', 'магазин розничной торговли'),
        ('Businessman', 'индивидуальный предприниматель')
    )

    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Адрес')

    type = models.CharField(max_length=20, choices=TYPE_LINK, default=FACTORY, verbose_name='тип звена')
    name = models.CharField(max_length=200, verbose_name='название')
    provider = models.ForeignKey('self', related_name='provider_link', on_delete=models.SET_NULL,
                                 **NULLABLE, verbose_name='поставщик')

    arrears = models.IntegerField(default=0, verbose_name='задолженность перед поставщиком в копейках')

    time_create = models.DateTimeField(verbose_name='время создания', default=datetime.now)


    def __str__(self):
        return f'{self.type}: название - {self.name}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
