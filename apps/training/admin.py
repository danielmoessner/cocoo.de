from django.contrib import admin
from .models import SeminarGroup, SeminarTopic, SeminarExecution


class SaveAsTrueAdmin(admin.ModelAdmin):
    save_as = True


class SeminarExecutionAdmin(SaveAsTrueAdmin):
    ordering = ('-start_date',)


admin.site.register(SeminarTopic, SaveAsTrueAdmin)
admin.site.register(SeminarExecution, SeminarExecutionAdmin)
admin.site.register(SeminarGroup, SaveAsTrueAdmin)
