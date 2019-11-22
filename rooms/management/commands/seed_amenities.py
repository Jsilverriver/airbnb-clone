from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):
    help = "This command tells me that he loves me"

    """def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you."
        )
        """

    def handle(self, *args, **options):
        """times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.WARNING("I love you"))
            """
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Wifi",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop friendly workspace",
            "TV",
            "Private bathroom",
            "Washer",
            "Dryer",
            "Breakfast",
            "Indoor fireplace",
            "Smoke detector",
            "Carbon monoxide detector",
        ]
        for a in amenities:
            room_models.Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities Created!"))
