from solo.models import SingletonModel
from django.db import models


class Image(models.Model):
    image = models.ImageField(verbose_name='Bild', upload_to='image/')
    alt = models.CharField(verbose_name='Titel', max_length=80)

    class Meta:
        verbose_name = 'Bild'
        verbose_name_plural = 'Bilder'

    def __str__(self):
        return '{}'.format(self.alt)

    @property
    def url(self):
        return self.image.url


class General(SingletonModel):
    company_name = models.CharField(verbose_name='Unternehmensname', max_length=100, default='CoCoo GmbH', blank=True)
    phone = models.CharField(verbose_name='Telefon', max_length=100, blank=True)
    email = models.CharField(verbose_name='E-Mail', max_length=100, blank=True)
    address_street = models.CharField(verbose_name='Adresse Straße', max_length=100, blank=True)
    address_city = models.CharField(verbose_name='Adresse Stadt', max_length=100, blank=True)
    help_statement = models.TextField(verbose_name='Statement', blank=True)
    
    email_use_tls = models.BooleanField(default=True)  
    email_host = models.CharField(max_length=255, blank=True, default='')
    email_host_user = models.CharField(max_length=255, blank=True, default='')
    email_host_password = models.CharField(max_length=255, blank=True, default='')
    email_port = models.IntegerField(default=587)

    default_from_email = models.CharField(
        max_length=255,
        blank=True,
        default='info@example.com',
        verbose_name="Absenderadresse (FROM)"
    )

    class Meta:
        verbose_name = 'Allgemein'

    def __str__(self):
        return 'Allgemein'

