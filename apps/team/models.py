from apps.settings.models import Image
from tinymce.models import HTMLField
from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Vorname')
    last_name = models.CharField(max_length=50, verbose_name='Nachname')
    slug = models.SlugField(verbose_name='Slug', unique=True,
                            help_text='Erscheint in der URL. Zum Beispiel: cocoo.de/team/max-mustermann/.')
    short_description = models.TextField(verbose_name='Kurzbeschreibung')
    description = HTMLField(verbose_name='Beschreibung')
    image = models.ImageField(upload_to='member/', verbose_name='Bild')
    #
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True, verbose_name="Entwurf")

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Mitarbeiter'
        verbose_name_plural = 'Mitarbeiter'

    def __str__(self):
        return self.name

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @staticmethod
    def all():
        return Member.objects.filter(draft=False)


class Certification(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    image = models.ForeignKey(Image, verbose_name='Bild', blank=True, null=True, on_delete=models.PROTECT)
    members = models.ManyToManyField(Member, verbose_name='Teammitglieder', related_name='certificates')
    #
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True, verbose_name="Entwurf")

    class Meta:
        ordering = ['name']
        verbose_name = 'Zertifikat'
        verbose_name_plural = 'Zertifikate'

    def __str__(self):
        return '{}'.format(self.name)

    @staticmethod
    def all():
        return Certification.objects.filter(draft=False)


class Book(models.Model):
    image = models.ImageField(verbose_name='Bild')
    title = models.CharField(max_length=100, verbose_name='Titel')
    description = models.TextField(verbose_name='Beschreibung')
    draft = models.BooleanField(default=True, verbose_name="Entwurf")

    class Meta:
        ordering = ['title']
        verbose_name = 'Buch'
        verbose_name_plural = 'Bücher'

    def __str__(self):
        return '{}'.format(self.title)

    @staticmethod
    def all():
        return Book.objects.filter(draft=False)
