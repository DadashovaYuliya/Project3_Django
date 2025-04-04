from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from mailings.forms import MailingForm
from mailings.models import Mailing
from recipient.models import Recipient


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_list.html'
    context_object_name = 'mailings'


class MailingDetailView(DetailView, LoginRequiredMixin):
    model = Mailing
    template_name = 'mailing_detail.html'
    context_object_name = 'mailing'


class MailingCreateView(CreateView, LoginRequiredMixin):
    model = Mailing
    form_class = MailingForm
    template_name = 'add_mailing.html'
    success_url = reverse_lazy('mailings:mailing_list')


class MailingUpdateView(UpdateView, LoginRequiredMixin):
    model = Mailing
    form_class = MailingForm
    template_name = 'add_mailing.html'
    success_url = reverse_lazy('mailings:mailing_list')


class MailingDeleteView(DeleteView, LoginRequiredMixin):
    model = Mailing
    template_name = 'mailing_confirm_delete.html'
    success_url = reverse_lazy('mailings:mailing_list')


def home_view(request):
    total_mail = Mailing.objects.count()
    active_mail = Mailing.objects.filter(status='LA').count()
    unique_recipients = Recipient.objects.values('email').distinct().count()

    context = {
        'total_mail': total_mail,
        'active_mail': active_mail,
        'unique_recipients': unique_recipients,
    }

    return render(request, 'home.html', context)