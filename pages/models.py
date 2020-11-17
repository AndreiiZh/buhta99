from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя заказчика')
    tel = models.CharField(max_length=256, verbose_name='Телефон заказчика')

    def __str__(self):
        return self.name
