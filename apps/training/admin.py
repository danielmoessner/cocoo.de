from django.contrib import admin
from .models import SeminarGroup, SeminarTopic, SeminarExecution


class SaveAsTrueAdmin(admin.ModelAdmin):
    save_as = True


admin.site.register(SeminarTopic, SaveAsTrueAdmin)
admin.site.register(SeminarExecution, SaveAsTrueAdmin)
admin.site.register(SeminarGroup, SaveAsTrueAdmin)
