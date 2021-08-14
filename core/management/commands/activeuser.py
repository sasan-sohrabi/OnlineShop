from argparse import ArgumentParser

from django.core.management import BaseCommand

from core.management.commands.baseuser import BaseUserCommand
from core.models import User


class Command(BaseCommand):

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('users', metavar='USERS', help='List of Users')
    
    def handle(self, *args, **options):
        user = User.objects.get(username=options['users'])
        user.is_active = True
        user.save()