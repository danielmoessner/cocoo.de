from django import forms
from apps.training.models import SeminarExecution


class ContactForm(forms.Form):
    first_name = forms.CharField(label='Vorname', required=True)
    last_name = forms.CharField(label='Nachname', required=True)
    email = forms.EmailField(label='E-Mail', required=True)
    message = forms.CharField(label='E-Mail', widget=forms.Textarea, required=True)
    business = forms.CharField(label='Honeypot', widget=forms.HiddenInput, required=True)
    data_protection = forms.BooleanField(label='Datenschutz', required=True)

    def get_data(self):
        data = ''
        for field in self.fields:
            field_data = '{}: {}'.format(self.fields[field].label, self.cleaned_data[field])
            data = '{}\n{}'.format(data, field_data)
        return data

    def clean_business(self):
        business = self.cleaned_data['business']
        if business != '3948':
            raise forms.ValidationError('Leider ist da etwas schief gegangen. '
                                        'Bitte schreiben Sie uns eine E-Mail. Vielen Dank.')
        return business


class SeminarRegistrationForm(forms.Form):
    seminar = forms.ModelChoiceField(SeminarExecution.objects.all())
    first_name = forms.CharField(label='Vorname', required=True)
    last_name = forms.CharField(label='Nachname', required=True)
    email = forms.EmailField(label='E-Mail', required=True)
    phone = forms.CharField(label='Telefon', required=True)
    amount_persons = forms.IntegerField(label='Anzahl Personen', required=True)
    data_protection = forms.BooleanField(label='Datenschutz', required=True)
    business = forms.CharField(label='Honeypot', widget=forms.HiddenInput, required=True)

    def get_data(self):
        data = ''
        for field in self.fields:
            field_data = '{}: {}'.format(self.fields[field].label, self.cleaned_data[field])
            data = '{}\n{}'.format(data, field_data)
        return data

    def clean_business(self):
        business = self.cleaned_data['business']
        if business != '3948':
            raise forms.ValidationError('Leider ist da etwas schief gegangen. '
                                        'Bitte schreiben Sie uns eine E-Mail. Vielen Dank.')
        return business
