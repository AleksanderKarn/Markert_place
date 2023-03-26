from django.db import models


class Contact(models.Model):
    email = models.EmailField(verbose_name='email поставщика')

    country = models.CharField(max_length=200, verbose_name='страна')
    city = models.CharField(max_length=200, verbose_name='город')
    street = models.CharField(max_length=200, verbose_name='улица')
    house_number = models.IntegerField(verbose_name='номер дома')

    def __str__(self):
        return f'Адрес: страна- {self.country}, город- {self.city},' \
               f' улица- {self.street}, дом- {self.house_number}. Email:{self.email}'

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'
