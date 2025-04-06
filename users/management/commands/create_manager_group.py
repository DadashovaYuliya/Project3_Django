from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Создает группу менеджеров и назначает ей необходимые права доступа'

    def create_manager_group(self, *args, **kwargs):
        manager_group = Group.objects.create(name='Manager')

        view_user_permission = Permission.objects.get(codename='view_user')
        view_recipient_permission = Permission.objects.get(codename='view_recipient')
        view_mailing_permission = Permission.objects.get(codename='view_mailing')
        block_permission = Permission.objects.get(codename='can_block_user')
        cancel_permission = Permission.objects.get(codename='can_cancel_mailing')

        manager_group.permissions.add(view_user_permission, view_recipient_permission, view_mailing_permission,
                                      block_permission, cancel_permission)

        manager_group.save()
