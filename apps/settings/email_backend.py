from django.core.mail.backends.smtp import EmailBackend
from django.db.utils import OperationalError, ProgrammingError
from django.conf import settings

from .models import General


class DbEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        general = General.get_solo()
        super().__init__(
            host=general.email_host,
            port=general.email_port,
            username=general.email_host_user,
            password=general.email_host_password,
            use_tls=general.email_use_tls,
        )
