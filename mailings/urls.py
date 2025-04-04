from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mailings.apps import MailingsConfig
from mailings.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, home_view

app_name = MailingsConfig.name

urlpatterns = [
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/new/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('home/', home_view, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
