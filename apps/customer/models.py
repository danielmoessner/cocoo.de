from django.db import models


class Testimonial(models.Model):
    testimonial = models.TextField(verbose_name='Rezension')
    customer = models.CharField(verbose_name='Kunde', max_length=50, blank=True)
    company = models.CharField(max_length=50, verbose_name='Firma', blank=True)
    #
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True, verbose_name="Entwurf")

    class Meta:
        ordering = ['testimonial']
        verbose_name = 'Referenz'
        verbose_name_plural = 'Referenzen'

    def __str__(self):
        return '{}'.format(self.testimonial[:100])

    @staticmethod
    def all():
        return Testimonial.objects.filter(draft=False)
