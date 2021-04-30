from solo.models import SingletonModel
from django.db import models


class General(SingletonModel):
    company_name = models.CharField(verbose_name='Unternehmensname', max_length=100, default='CoCoo GmbH', blank=True)
    phone = models.CharField(verbose_name='Telefon', max_length=100, blank=True)
    email = models.CharField(verbose_name='E-Mail', max_length=100, blank=True)
    address_street = models.CharField(verbose_name='Adresse Straße', max_length=100, blank=True)
    address_city = models.CharField(verbose_name='Adresse Stadt', max_length=100, blank=True)
    help_statement = models.TextField(verbose_name='Statement', blank=True)

    class Meta:
        verbose_name = 'Allgemein'

    def __str__(self):
        return 'Allgemein'
