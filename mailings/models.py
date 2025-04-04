from django.db import models

from message.models import Message
from recipient.models import Recipient


class Mailing(models.Model):
    COMPLETED = 'CO'
    CREATED = 'CR'
    LAUNCHED = 'LA'

    STATUS_CHOICES = {
        COMPLETED: 'Завершена',
        CREATED: 'Создана',
        LAUNCHED: 'Запущена',
    }

    first_dispatch = models.DateTimeField(verbose_name='Дата и время первой отправки', help_text='yyyy-mm-dd 00:00:00')
    end_dispatch = models.DateTimeField(verbose_name='Дата и время окончания отправки', help_text='yyyy-mm-dd 00:00:00')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение', related_name='message')
    recipients = models.ManyToManyField(Recipient, verbose_name='Получатели', related_name='recipients')


    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status', 'first_dispatch', 'message',]

    def __str__(self):
        return self.status

class MailingAttempt(models.Model):
    SUCCESSFULLY = 'SU'
    FAILED = 'FA'

    STATUS_ATTEMPT_CHOICES = {
        SUCCESSFULLY: 'Успешно',
        FAILED: 'Не успешно',
    }

    date_attempt = models.DateTimeField(verbose_name='Дата и время попытки', help_text='yyyy-mm-dd 00:00:00')
    status = models.CharField(max_length=20, choices=STATUS_ATTEMPT_CHOICES, verbose_name='Статус')
    mail_response = models.TextField(verbose_name='Ответ почтового сервера')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка', related_name='mailing')

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'
        ordering = ['status', 'date_attempt',]

    def __str__(self):
        return f'{self.date_attempt} - {self.status}'
