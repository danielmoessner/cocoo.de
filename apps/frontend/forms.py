from django import forms
from apps.training.models import SeminarExecution, SeminarTopic


class ContactForm(forms.Form):
    first_name = forms.CharField(label='Vorname', required=True)
    last_name = forms.CharField(label='Nachname', required=True)
    email = forms.EmailField(label='E-Mail', required=True)
    message = forms.CharField(label='Nachricht', widget=forms.Textarea, required=True)
    honey1234 = forms.CharField(label='Honeypot', widget=forms.HiddenInput(attrs={"autocomplete": "off"}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].label = self.fields[field].label + '*'

    def get_data(self):
        data = ''
        for field in self.fields:
            field_data = '{}: {}'.format(self.fields[field].label, self.cleaned_data[field])
            data = '{}\n{}'.format(data, field_data)
        return data

    def clean_honey1234(self):
        business = self.cleaned_data['honey1234']
        if business != '3948':
            raise forms.ValidationError('Leider ist da etwas schief gegangen. '
                                        'Bitte schreiben Sie uns eine E-Mail. Vielen Dank.')
        return business


class SeminarRegistrationForm(forms.Form):
    seminar = forms.ModelChoiceField(SeminarExecution.objects.exclude(status='FULL'), empty_label='Inhouse',
                                     required=False, label='Seminar')
    first_name = forms.CharField(label='Vorname', required=True)
    last_name = forms.CharField(label='Nachname', required=True)
    email = forms.EmailField(label='E-Mail', required=True)
    phone = forms.CharField(label='Telefon', required=True)
    amount_persons = forms.IntegerField(label='Anzahl Personen', required=True)
    honey1234 = forms.CharField(label='Honeypot', widget=forms.HiddenInput, required=True)
    topic = forms.ModelChoiceField(label='Seminarthema', widget=forms.HiddenInput, queryset=SeminarTopic.objects.all())
    message = forms.CharField(label='Nachricht', widget=forms.Textarea(attrs={'rows': 4, 'cols': 10}), required=False)

    def __init__(self, seminartopic=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if seminartopic:
            self.fields['topic'].initial = seminartopic
            self.fields['seminar'].queryset = self.fields['seminar'].queryset.filter(topic=seminartopic)
        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].label = self.fields[field].label + '*'

    def get_data(self):
        data = ''
        for field in self.fields:
            field_data = '{}: {}'.format(self.fields[field].label, self.cleaned_data[field])
            data = '{}\n{}'.format(data, field_data)
        return data

    def clean_honey1234(self):
        business = self.cleaned_data['honey1234']
        if business != '3948':
            raise forms.ValidationError('Leider ist da etwas schief gegangen. '
                                        'Bitte schreiben Sie uns eine E-Mail. Vielen Dank.')
        return business

    def clean_seminar(self):
        seminar = self.cleaned_data['seminar']
        if seminar is None:
            return 'Inhouse'
        return seminar
