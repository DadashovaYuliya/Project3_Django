import secrets

from django.conf import settings
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, CustomPasswordResetForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(15)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение электронного адреса',
            message=f'Спасибо за регистрацию на нашем сайте. Подвердите адрес электронной почты, перейдя по следующей ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect('users:login')

# class CustomPasswordResetView(PasswordResetView):
#     """Восстановление пароля"""
#     template_name = 'users/password_reset_request.html'
#     form_class = CustomPasswordResetForm
#     success_url = reverse_lazy('users:password_reset_done')
#     title = "Сброс пароля"
#     email_template_name = 'users/password_reset_email.html'
#     from_email = settings.EMAIL_HOST_USER
