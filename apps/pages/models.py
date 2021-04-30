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


class Contact(SingletonModel):
    header_heading = models.CharField(verbose_name='Header Überschrift', max_length=60, blank=True)
    header_text = models.CharField(verbose_name='Header Text', max_length=200, blank=True)
    header_image = models.ImageField(verbose_name='Header Bild', upload_to='contact/')
    contact_heading = models.CharField(verbose_name='Kontakt Überschrift', max_length=80, blank=True)
    contact_emailphone = models.CharField(verbose_name='E-Mail und Telefon Überschrift', max_length=50, blank=True)
    contact_address = models.CharField(verbose_name='Adresse Überschrift', max_length=50, blank=True)
    form_heading = models.CharField(verbose_name='Formular Überschrift', max_length=80, blank=True)
    form_buttontext = models.CharField(verbose_name='Formular Button Text', max_length=100, blank=True)
    form_dataprotectiontext = models.CharField(verbose_name='Formular Datenschutz Text', max_length=200, blank=True)
    form_successheading = models.CharField(verbose_name='Formular Abgeschickt Überschrift', max_length=100, blank=True)
    form_successtext = models.CharField(verbose_name='Formular Abgeschickt Text', max_length=300, blank=True)
    form_successlink = models.CharField(verbose_name='Formular Abgeschickt Linktext', max_length=80, blank=True)

    class Meta:
        verbose_name = 'Kontakt'

    def __str__(self):
        return 'Kontakt'


class Team(SingletonModel):
    header_heading = models.CharField(verbose_name='Header Überschrift', max_length=60, blank=True)
    header_text = models.CharField(verbose_name='Header Text', max_length=200, blank=True)
    header_image = models.ImageField(verbose_name='Header Bild', upload_to='team/')
    about_heading = models.CharField(verbose_name='Über uns Überschrift', max_length=100, blank=True)
    about_text = HTMLField(verbose_name='Über uns Text')
    team_heading = models.CharField(verbose_name='Team Überschrift', max_length=100, blank=True)
    books_heading = models.CharField(verbose_name='Bücher Überschrift', max_length=100, blank=True)
    books_subheading = models.CharField(verbose_name='Bücher Unterüberschrift', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Team'

    def __str__(self):
        return 'Team'


class Seminars(SingletonModel):
    header_heading = models.CharField(verbose_name='Header Überschrift', max_length=60, blank=True)
    header_text = models.CharField(verbose_name='Header Text', max_length=200, blank=True)
    header_image = models.ImageField(verbose_name='Header Bild', upload_to='seminartopiclist/')

    class Meta:
        verbose_name = 'Seminare'

    def __str__(self):
        return 'Seminare'


class Index(SingletonModel):
    header_heading = models.CharField(verbose_name='Header Überschrift', max_length=60, blank=True)
    header_headingred = models.CharField(verbose_name='Header Überschrift Rot', max_length=200, blank=True)
    header_text = models.CharField(verbose_name='Header Text', max_length=200, blank=True)
    header_image = models.ImageField(verbose_name='Header Bild', upload_to='index/')
    header_buttonleft = models.CharField(verbose_name='Header Button Links', max_length=50, blank=True)
    header_buttonright = models.CharField(verbose_name='Header Button Rechts', max_length=50, blank=True)
    intro_pretitle = models.CharField(verbose_name='Intro Vorüberschrift', max_length=200, blank=True)
    intro_title = models.CharField(verbose_name='Intro Überschrift', max_length=200, blank=True)
    intro_subtitle = models.CharField(verbose_name='Intro Unterüberschrift', max_length=200, blank=True)
    intro_leftheading = models.CharField(verbose_name='Intro Überschrift Links', max_length=200, blank=True)
    intro_lefttext = models.TextField(verbose_name='Intro Text Links')
    intro_leftbutton = models.CharField(verbose_name='Intro Button Links', max_length=200, blank=True)
    intro_rightheading = models.CharField(verbose_name='Intro Überschrift Rechts', max_length=200, blank=True)
    intro_righttext = models.TextField(verbose_name='Intro Text Rechts')
    intro_rightbutton = models.CharField(verbose_name='Intro Button Rechts', max_length=200, blank=True)
    seminars_heading = models.CharField(verbose_name='Seminare Überschrift', max_length=100, blank=True)
    testimonials_heading = models.CharField(verbose_name='Referenzen Überschrift', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Startseite'

    def __str__(self):
        return 'Startseite'


class Coaching(SingletonModel):
    header_heading = models.CharField(verbose_name='Header Überschrift', max_length=60, blank=True)
    header_text = models.CharField(verbose_name='Header Text', max_length=200, blank=True)
    header_image = models.ImageField(verbose_name='Header Bild', upload_to='team/')
    content = HTMLField(verbose_name='Inhalt')

    class Meta:
        verbose_name = 'Coaching'

    def __str__(self):
        return 'Coaching'


class Seminar(SingletonModel):
    content_pretitle = models.CharField(verbose_name='Inhalt Vortitel', max_length=80, blank=True)
    content_title = models.CharField(verbose_name='Inhalt Titel', max_length=80, blank=True)
    infos_title = models.CharField(verbose_name='Infos Titel', max_length=80, blank=True)
    infos_subtitle1 = models.CharField(verbose_name='Infos Untertitel 1', max_length=80, blank=True)
    infos_subtitle2 = models.CharField(verbose_name='Infos Untertitel 2', max_length=80, blank=True)
    infos_subtitle3 = models.CharField(verbose_name='Infos Untertitel 3', max_length=80, blank=True)
    seminars_title = models.CharField(verbose_name='Seminare Titel', max_length=80, blank=True)
    form_title = models.CharField(verbose_name='Formular Titel', max_length=80, blank=True)
    form_text = models.CharField(verbose_name='Formular Text', max_length=140, blank=True)
    form_dataprotection = models.CharField(verbose_name='Formular Datenschutz Text', max_length=200, blank=True)
    form_requiredfields = models.CharField(verbose_name='Formular Muss Felder Text', max_length=200, blank=True)
    form_button = models.CharField(verbose_name='Formular Button', max_length=200, blank=True)
    form_successtitle = models.CharField(verbose_name='Formular Erfolg Titel', max_length=80, blank=True)
    form_successtext = models.TextField(verbose_name='Formular Erfolg Text')
    form_successbutton = models.CharField(verbose_name='Formular Erfolg Button', max_length=80, blank=True)

    class Meta:
        verbose_name = 'Seminar'

    def __str__(self):
        return 'Seminar'


class Member(SingletonModel):
    content_pretitle = models.CharField(verbose_name='Inhalt Vortitel', max_length=80, blank=True)
    content_title = models.CharField(verbose_name='Inhalt Titel', max_length=80, blank=True)

    class Meta:
        verbose_name = 'Teammitglied'

    def __str__(self):
        return 'Teammitglied'
