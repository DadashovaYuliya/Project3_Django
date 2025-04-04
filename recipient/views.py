from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from recipient.forms import RecipientForm
from recipient.models import Recipient


class RecipientListView(ListView):
    model = Recipient
    template_name = 'recipient_list.html'
    context_object_name = 'recipients'


class RecipientDetailView(DetailView, LoginRequiredMixin):
    model = Recipient
    template_name = 'recipient_detail.html'
    context_object_name = 'recipient'


class RecipientCreateView(CreateView, LoginRequiredMixin):
    model = Recipient
    form_class = RecipientForm
    template_name = 'add_recipient.html'
    success_url = reverse_lazy('recipient:recipient_list')


class RecipientUpdateView(UpdateView, LoginRequiredMixin):
    model = Recipient
    form_class = RecipientForm
    template_name = 'add_recipient.html'
    success_url = reverse_lazy('recipient:recipient_list')


class RecipientDeleteView(DeleteView, LoginRequiredMixin):
    model = Recipient
    template_name = 'recipient_confirm_delete.html'
    success_url = reverse_lazy('recipient:recipient_list')
