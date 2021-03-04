from django.contrib import admin
from .models import SeminarGroup, SeminarTopic, SeminarExecution


admin.site.register(SeminarTopic)
admin.site.register(SeminarExecution)
admin.site.register(SeminarGroup)
