from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from message.forms import MessageForm
from message.models import Message


class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'


class MessageDetailView(DetailView, LoginRequiredMixin):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'


class MessageCreateView(CreateView, LoginRequiredMixin):
    model = Message
    form_class = MessageForm
    template_name = 'add_message.html'
    success_url = reverse_lazy('message:message_list')


class MessageUpdateView(UpdateView, LoginRequiredMixin):
    model = Message
    form_class = MessageForm
    template_name = 'add_message.html'
    success_url = reverse_lazy('message:message_list')


class MessageDeleteView(DeleteView, LoginRequiredMixin):
    model = Message
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy('message:message_list')
