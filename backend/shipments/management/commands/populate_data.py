from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from shipments.factories import UserFactory
from users.models import User


class Command(BaseCommand):
    help = "Populate data for shipments"

    def handle(self, *args, **options):
        faker = Faker()
        for i in range(1, 10):
            user = UserFactory.create()
