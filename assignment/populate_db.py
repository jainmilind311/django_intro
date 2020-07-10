import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')

import django

django.setup()


from faker import Faker
from display_user.models import User

fake_gen = Faker()


def generate_users(N=10):

    for i in range(N):
        name = fake_gen.name()
        first_name = name.split()[0]
        last_name = name.split()[1]
        email = fake_gen.email()

        usr = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]



if __name__ == "__main__":
    print('Started generating Users')
    generate_users(30)
    print('Finished!')