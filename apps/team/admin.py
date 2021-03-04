from django.contrib import admin
from .models import Member
from .models import Certification


admin.site.register(Certification)
admin.site.register(Member)
