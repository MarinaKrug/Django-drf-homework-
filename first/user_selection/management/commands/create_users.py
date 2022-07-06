from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create users'

    def create(self):

        User.objects.create_user(role_choice='Пользователь', Avatar='user_selection/images/user.png')
        User.objects.create_user(role_choice='CRM - администратор', Avatar='user_selection/images/crm_admin.png')
        User.objects.create_user(role_choice='менеджер', Avatar='user_selection/images/admin.png')
