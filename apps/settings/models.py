from tinymce.models import HTMLField
from solo.models import SingletonModel


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
