from argparse import ArgumentParser

from django.core.management import BaseCommand

from core.models import User


class BaseUserCommand(BaseCommand):

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('users', metavar='USERS', help='List of Users')


    def handle(self, *args, **options):
        user = User.objects.get(username=options['users'])
        print(user)