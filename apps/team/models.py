from django.db import models
from tinymce.models import HTMLField


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


class Certification(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    image = models.ImageField(verbose_name='Bild', upload_to='certification/', blank=True)
    member = models.ForeignKey(Member, verbose_name='Teammitglied', on_delete=models.CASCADE)
    #
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True, verbose_name="Entwurf")

    class Meta:
        ordering = ['member']
        verbose_name = 'Zertifikat'
        verbose_name_plural = 'Zertifikate'

    def __str__(self):
        return '{}'.format(self.name)