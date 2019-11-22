import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many times do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = (
            user_models.User.objects.all()
        )  # 지금은 50개정도의 유저만 갖고 있기 때문에 이게 가능한것!! 주의! 데이터베이스가 크면 사용하지 못함!
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "host": lambda x: random.choice(all_users),
                # lambda는 익명의 함수. 자바스크립트의 (x) => asdfasdf 이런...거라고 하는데 뭔말? #random하게 host를 선택하게 해줌.
                "room_type": lambda x: random.choice(room_types),
                # Field rooms.Room.room_type cannot be null
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms Created!"))
