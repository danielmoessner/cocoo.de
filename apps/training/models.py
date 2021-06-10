from apps.settings.models import Image
from apps.team.models import Member
from tinymce.models import HTMLField
from django.db import models


class SeminarGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Beschreibung', blank=True)
    slug = models.SlugField(verbose_name='Slug', unique=True,
                            help_text='Erscheint in der URL. Zum Beispiel: cocoo.de/seminargruppe/scrum/.')
    #
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True, verbose_name="Entwurf")

    class Meta:
        ordering = ['slug']
        verbose_name = 'Seminargruppe'
        verbose_name_plural = 'Seminargruppen'

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        super().save(*args, **kwargs)

    @property
    def topics_sorted(self):
        return self.seminar_topics.order_by('-title')

    @staticmethod
    def all():
        return SeminarGroup.objects.filter(draft=False)


class SeminarTopic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Name')
    slug = models.SlugField(verbose_name='Slug', unique=True,
                            help_text='Erscheint in der URL. Zum Beispiel: '
                                      'cocoo.de/seminarthema/certified-less-practitioner/.')
    short_description = models.TextField(verbose_name='Kurzbeschreibung')
    description = HTMLField(verbose_name='Beschreibung')
    image = models.ForeignKey(Image, verbose_name='Bild', blank=True, null=True, on_delete=models.PROTECT)
    certificate = models.TextField(verbose_name='Zertifikatsaussage')
    languages = models.TextField(verbose_name='Sprachen')
    executions = models.TextField(verbose_name='Durchführungen')
    seminar_group = models.ForeignKey(SeminarGroup, related_name='seminar_topics', verbose_name='Seminargruppe',
                                      on_delete=models.PROTECT)
    promotions = models.TextField(verbose_name='Rabattaktionen', blank=True)

    #
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True, verbose_name="Entwurf")

    class Meta:
        ordering = ['slug']
        verbose_name = 'Seminarthema'
        verbose_name_plural = 'Seminarthemen'

    def __str__(self):
        return '{}'.format(self.title)

    @staticmethod
    def all():
        return SeminarTopic.objects.filter(draft=False)


class SeminarExecution(models.Model):
    topic = models.ForeignKey(SeminarTopic, verbose_name='Thema', on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='Startdatum')
    end_date = models.DateField(verbose_name='Enddatum')
    location = models.CharField(max_length=50, verbose_name='Ort', blank=True)
    execution_choices = (
        ('PRESENCE', 'Präsenz'),
        ('VIRTUAL', 'Virtuell')
    )
    execution = models.CharField(choices=execution_choices, verbose_name='Durchführung', max_length=40)
    language = models.CharField(max_length=50, verbose_name='Sprache')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preis', null=True, blank=True)
    early_booking_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Frühbucherpreis', null=True,
                                              blank=True)
    show_early_booking_price = models.BooleanField(verbose_name='Frühbucherpreis anzeigen')
    execution_hours = models.TextField(verbose_name='Durchführungszeiten')
    STATUS_CHOICES = (
        ('OPEN', 'Plätze verfügbar'),
        ('ALMOST_FULL', 'Wenige Plätze verfügbar'),
        ('FULL', 'Ausgebucht')
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, verbose_name='Buchungsstatus')
    members = models.ManyToManyField(Member, verbose_name='Teammitglieder', blank=True)
    show_on_index = models.BooleanField(verbose_name='Auf der Startseite im Slider anzeigen', default=True)
    #
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True, verbose_name="Entwurf")

    class Meta:
        ordering = ['start_date']
        verbose_name = 'Seminardurchführung'
        verbose_name_plural = 'Seminardurchführungen'

    def __str__(self):
        return '{} - {}: {}'.format(self.start_date.strftime('%d.%m.%Y'),
                                    self.end_date.strftime('%d.%m.%Y'), self.topic.title)

    @staticmethod
    def all():
        return SeminarExecution.objects.filter(draft=False)
