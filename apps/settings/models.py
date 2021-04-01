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
    help_statement = models.TextField(verbose_name='Statement', blank=True)

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


class Team(SingletonModel):
    header_heading = models.CharField(verbose_name='Header Überschrift', max_length=60)
    header_text = models.CharField(verbose_name='Header Text', max_length=200)
    header_image = models.ImageField(verbose_name='Header Bild', upload_to='team/')
    about_heading = models.CharField(verbose_name='Über uns Überschrift', max_length=100)
    about_text = HTMLField(verbose_name='Über uns Text')
    team_heading = models.CharField(verbose_name='Team Überschrift', max_length=100)
    books_heading = models.CharField(verbose_name='Bücher Überschrift', max_length=100)
    books_subheading = models.CharField(verbose_name='Bücher Unterüberschrift', max_length=200)

    class Meta:
        verbose_name = 'Team'

    def __str__(self):
        return 'Team'


class Seminars(SingletonModel):
    header_heading = models.CharField(verbose_name='Header Überschrift', max_length=60)
    header_text = models.CharField(verbose_name='Header Text', max_length=200)
    header_image = models.ImageField(verbose_name='Header Bild', upload_to='seminartopiclist/')

    class Meta:
        verbose_name = 'Seminare'

    def __str__(self):
        return 'Seminare'


class Index(SingletonModel):
    header_heading = models.CharField(verbose_name='Header Überschrift', max_length=60)
    header_headingred = models.CharField(verbose_name='Header Überschrift Rot', max_length=200, blank=True)
    header_text = models.CharField(verbose_name='Header Text', max_length=200)
    header_image = models.ImageField(verbose_name='Header Bild', upload_to='index/')
    header_buttonleft = models.CharField(verbose_name='Header Button Links', max_length=50)
    header_buttonright = models.CharField(verbose_name='Header Button Rechts', max_length=50)
    intro_pretitle = models.CharField(verbose_name='Intro Vorüberschrift', max_length=200)
    intro_title = models.CharField(verbose_name='Intro Überschrift', max_length=200)
    intro_subtitle = models.CharField(verbose_name='Intro Unterüberschrift', max_length=200)
    intro_leftheading = models.CharField(verbose_name='Intro Überschrift Links', max_length=200)
    intro_lefttext = models.TextField(verbose_name='Intro Text Links')
    intro_leftbutton = models.CharField(verbose_name='Intro Button Links', max_length=200)
    intro_rightheading = models.CharField(verbose_name='Intro Überschrift Rechts', max_length=200)
    intro_righttext = models.TextField(verbose_name='Intro Text Rechts')
    intro_rightbutton = models.CharField(verbose_name='Intro Button Rechts', max_length=200)
    seminars_heading = models.CharField(verbose_name='Seminare Überschrift', max_length=100)
    testimonials_heading = models.CharField(verbose_name='Referenzen Überschrift', max_length=100)

    class Meta:
        verbose_name = 'Startseite'

    def __str__(self):
        return 'Startseite'


class Coaching(SingletonModel):
    header_heading = models.CharField(verbose_name='Header Überschrift', max_length=60)
    header_text = models.CharField(verbose_name='Header Text', max_length=200)
    header_image = models.ImageField(verbose_name='Header Bild', upload_to='team/')
    content = HTMLField(verbose_name='Inhalt')

    class Meta:
        verbose_name = 'Coaching'

    def __str__(self):
        return 'Coaching'
