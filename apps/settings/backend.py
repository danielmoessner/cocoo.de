
from django.core.mail.backends.smtp import EmailBackend
from django.db.utils import OperationalError, ProgrammingError
from django.conf import settings

from .models import General

class DbEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            general = General.get_solo()

            if general.email_host:
                self.host = general.email_host
            if general.email_port:
                self.port = general.email_port
            if general.email_host_user:
                self.username = general.email_host_user
            if general.email_host_password:
                self.password = general.email_host_password
            self.use_tls = general.email_use_tls

           
            if general.default_from_email:
                settings.DEFAULT_FROM_EMAIL = general.default_from_email

        except (OperationalError, ProgrammingError):

            pass