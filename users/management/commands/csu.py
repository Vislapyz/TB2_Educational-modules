from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создания superuser"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@sky.pro",
            is_superuser=True,
            is_staff=True,
        )
        user.set_password("123qweQWE")
        user.save()
