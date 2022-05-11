from apps.pages.models import Imprint, DataProtection, Contact, Index, Seminars, Team, Coaching, Seminar, \
    Member
from tinymce.widgets import TinyMCE
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from django import forms

mce_config = {
    'block_formats': 'Paragraph=p; H1=h1; H2=h2; H3=h3; Vorformatiert=pre'
}


class ImprintForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(mce_attrs=mce_config))

    class Meta:
        fields = '__all__'
        model = Imprint


class ImprintModelAdmin(SingletonModelAdmin):
    form = ImprintForm


admin.site.register(Imprint, ImprintModelAdmin)


class DataProtectionForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(mce_attrs=mce_config))

    class Meta:
        fields = '__all__'
        model = DataProtection


class DataProtectionModelAdmin(SingletonModelAdmin):
    form = DataProtectionForm


admin.site.register(DataProtection, DataProtectionModelAdmin)
admin.site.register(Contact, SingletonModelAdmin)
admin.site.register(Index, SingletonModelAdmin)
admin.site.register(Seminars, SingletonModelAdmin)
admin.site.register(Team, SingletonModelAdmin)
admin.site.register(Coaching, SingletonModelAdmin)
admin.site.register(Seminar, SingletonModelAdmin)
admin.site.register(Member, SingletonModelAdmin)
