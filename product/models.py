from django.db import models

from link_model.models import Provider


class Product(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name='Поставщик')

    name = models.CharField(max_length=200, verbose_name='название продукта')
    model = models.CharField(max_length=200, verbose_name='модель')
    data_publicate = models.DateTimeField(verbose_name='дата выхода продукта')

    def __str__(self):
        return f'Продукт - {self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
