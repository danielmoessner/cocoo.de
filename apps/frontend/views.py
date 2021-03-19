from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse
from django.views import generic

from apps.customer.models import Testimonial
from apps.frontend.forms import ContactForm
from apps.settings.models import Imprint, DataProtection, Contact, General
from apps.team.models import Member
from apps.training.models import SeminarGroup, SeminarExecution, SeminarTopic


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'frontend/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_groups'] = SeminarGroup.objects.all()
        context['seminar_executions'] = SeminarExecution.objects.all()
        context['members'] = Member.objects.all()
        context['testimonial'] = Testimonial.objects.order_by('?').first()
        return context


class MemberListView(LoginRequiredMixin, generic.ListView):
    template_name = 'frontend/member/list.html'
    model = Member

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_groups'] = SeminarGroup.objects.all()
        return context


class ContactView(LoginRequiredMixin, generic.FormView):
    template_name = 'frontend/contact.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_groups'] = SeminarGroup.objects.all()
        context['page'] = Contact.get_solo()
        context['general'] = General.get_solo()
        return context

    def form_valid(self, form):
        message = form.get_data()
        subject = 'Anfrage über das Kontaktformular auf cocoo.de'
        sender = settings.DEFAULT_FROM_EMAIL
        recipient = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, sender, [recipient])
        context = self.get_context_data(form=form)
        context['success'] = True
        return self.render_to_response(context)


class ImprintView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'frontend/imprint.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Imprint.objects.get()
        context['seminar_groups'] = SeminarGroup.objects.all()
        return context


class DateProtectionView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'frontend/data_protection.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = DataProtection.objects.get()
        context['seminar_groups'] = SeminarGroup.objects.all()
        return context


class SeminarGroupListView(LoginRequiredMixin, generic.ListView):
    model = SeminarGroup
    template_name = 'frontend/seminargroup/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_groups'] = SeminarGroup.objects.all()
        return context


class SeminarTopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = SeminarTopic
    template_name = 'frontend/seminartopic/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_groups'] = SeminarGroup.objects.all()
        context['seminar_executions'] = SeminarExecution.objects.filter(topic=self.object)
        return context


class MemberDetailView(LoginRequiredMixin, generic.DetailView):
    model = Member
    template_name = 'frontend/member/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_groups'] = SeminarGroup.objects.all()
        return context
