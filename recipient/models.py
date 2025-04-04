from django.db import models

class Recipient(models.Model):
    email = models.CharField(max_length=50, unique=True, verbose_name='Email')
    full_name = models.CharField(max_length=150, verbose_name='Ф.И.О.')
    comment = models.TextField(verbose_name='Комментарий')


    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'
        ordering = ['full_name']

    def __str__(self):
        return self.full_name
