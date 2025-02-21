
from django.core.mail.backends.smtp import EmailBackend
from django.db.utils import OperationalError, ProgrammingError
from django.conf import settings

from .models import General

class DbEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            general = General.get_solo()
            self.host = general.email_host or self.host
            self.port = general.email_port or self.port
            self.username = general.email_host_user or self.username
            self.password = general.email_host_password or self.password
            self.use_tls = general.email_use_tls
            settings.DEFAULT_FROM_EMAIL = general.default_from_email or settings.DEFAULT_FROM_EMAIL
        except (OperationalError, ProgrammingError):
            pass
