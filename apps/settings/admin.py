from django.contrib import admin
from apps.settings.models import General, Image
from solo.admin import SingletonModelAdmin


admin.site.register(Image)
admin.site.register(General, SingletonModelAdmin)
