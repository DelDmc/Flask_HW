from faker import Faker
from faker.providers import BaseProvider

fake = Faker("UK")


class HWProvider(BaseProvider):
    def profile_for_homework(self):
        return {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(),
            'date_of_birth': str(fake.date_of_birth(None, 17, 25, ))
        }


fake.add_provider(HWProvider)

