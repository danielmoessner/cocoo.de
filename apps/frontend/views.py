from django.contrib.auth.mixins import LoginRequiredMixin
from apps.training.models import SeminarGroup, SeminarExecution, SeminarTopic
from apps.settings.models import General
from apps.pages.models import Imprint, DataProtection, Contact, Team, Index, Seminars, Coaching, Seminar, \
    Member as MemberPage
from apps.customer.models import Testimonial
from apps.frontend.forms import ContactForm, SeminarRegistrationForm
from apps.team.models import Member, Book
from django.core.mail import send_mail
from django.views import generic
from django.urls import reverse
from django.conf import settings


# mixins
class AllContextMixin(generic.base.ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['general'] = General.get_solo()
        context['seminar_groups'] = SeminarGroup.objects.all()
        return context


# views
class IndexView(LoginRequiredMixin, AllContextMixin, generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_groups'] = SeminarGroup.objects.all()
        context['seminar_executions'] = SeminarExecution.objects.filter(show_on_index=True)
        context['members'] = Member.objects.all()
        context['testimonials'] = Testimonial.objects.order_by('?')
        context['page'] = Index.get_solo()
        return context


class MemberListView(LoginRequiredMixin, AllContextMixin, generic.ListView):
    template_name = 'team.html'
    model = Member

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_groups'] = SeminarGroup.objects.all()
        context['books'] = Book.objects.all()
        context['page'] = Team.get_solo()
        return context


class ContactView(LoginRequiredMixin, AllContextMixin, generic.FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contact')+'?erfolg=True#erfolg'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_groups'] = SeminarGroup.objects.all()
        context['page'] = Contact.get_solo()
        context['success'] = self.request.GET.get('erfolg', default=None)
        return context

    def form_valid(self, form):
        message = form.get_data()
        subject = 'Anfrage über das Kontaktformular auf cocoo.de'
        sender = settings.DEFAULT_FROM_EMAIL
        recipient = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, sender, [recipient])
        return super().form_valid(form)


class ImprintView(LoginRequiredMixin, AllContextMixin, generic.TemplateView):
    template_name = 'imprint.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Imprint.get_solo()
        context['seminar_groups'] = SeminarGroup.objects.all()
        return context


class DataProtectionView(LoginRequiredMixin, AllContextMixin, generic.TemplateView):
    template_name = 'data_protection.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = DataProtection.get_solo()
        context['seminar_groups'] = SeminarGroup.objects.all()
        return context


class SeminarGroupListView(LoginRequiredMixin, AllContextMixin, generic.ListView):
    model = SeminarGroup
    template_name = 'seminargroups.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_groups'] = SeminarGroup.objects.all()
        context['page'] = Seminars.get_solo()
        return context


class SeminarTopicDetailView(LoginRequiredMixin, AllContextMixin, generic.detail.SingleObjectMixin,
                             generic.FormView):
    model = SeminarTopic
    template_name = 'seminar.html'
    form_class = SeminarRegistrationForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['seminartopic'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse('seminartopic_detail', args=[self.object.slug])+'?erfolg=True#erfolg'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Seminar.get_solo()
        context['seminar_executions'] = SeminarExecution.objects.filter(topic=self.object)
        context['success'] = self.request.GET.get('erfolg', default=None)
        return context

    def form_valid(self, form):
        message = form.get_data()
        subject = 'Anfrage über das Seminarformular auf cocoo.de'
        sender = settings.DEFAULT_FROM_EMAIL
        recipient = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, sender, [recipient])
        return super().form_valid(form)


class MemberDetailView(LoginRequiredMixin, AllContextMixin, generic.DetailView):
    model = Member
    template_name = 'member.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = MemberPage.get_solo()
        context['seminar_groups'] = SeminarGroup.objects.all()
        return context


class CoachingView(LoginRequiredMixin, AllContextMixin, generic.TemplateView):
    template_name = 'coaching.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Coaching.get_solo()
        return context
