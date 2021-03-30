from tinymce.models import HTMLField
from solo.models import SingletonModel
from django.db import models


class Imprint(SingletonModel):
    text = HTMLField(verbose_name='Inhalt')

    class Meta:
        verbose_name = "Impressum"

    def __str__(self):
        return 'Impressum'


class DataProtection(SingletonModel):
    text = HTMLField(verbose_name='Inhalt')

    class Meta:
        verbose_name = "Datenschutz"

    def __str__(self):
        return 'Datenschutz'


class General(SingletonModel):
    company_name = models.CharField(verbose_name='Unternehmensname', max_length=100, default='CoCoo GmbH')
    phone = models.CharField(verbose_name='Telefon', max_length=100)
    email = models.CharField(verbose_name='E-Mail', max_length=100)
    address_street = models.CharField(verbose_name='Adresse Straße', max_length=100)
    address_city = models.CharField(verbose_name='Adresse Stadt', max_length=100)

    class Meta:
        verbose_name = 'Allgemein'

    def __str__(self):
        return 'Allgemein'


class Contact(SingletonModel):
    header_heading = models.CharField(verbose_name='Header Überschrift', max_length=60)
    header_text = models.CharField(verbose_name='Header Text', max_length=200)
    header_image = models.ImageField(verbose_name='Header Bild', upload_to='contact/')
    contact_heading = models.CharField(verbose_name='Kontakt Überschrift', max_length=80)
    contact_emailphone = models.CharField(verbose_name='E-Mail und Telefon Überschrift', max_length=50)
    contact_address = models.CharField(verbose_name='Adresse Überschrift', max_length=50)
    form_heading = models.CharField(verbose_name='Formular Überschrift', max_length=80)
    form_buttontext = models.CharField(verbose_name='Formular Button Text', max_length=100)
    form_dataprotectiontext = models.CharField(verbose_name='Formular Datenschutz Text', max_length=200)
    form_successheading = models.CharField(verbose_name='Formular Abgeschickt Überschrift', max_length=100)
    form_successtext = models.CharField(verbose_name='Formular Abgeschickt Text', max_length=300)
    form_successlink = models.CharField(verbose_name='Formular Abgeschickt Linktext', max_length=80)


    class Meta:
        verbose_name = 'Kontakt'

    def __str__(self):
        return 'Kontakt'
