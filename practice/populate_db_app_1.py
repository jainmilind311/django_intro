import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice.settings')

import django
django.setup()

from faker import Faker
import random
from app_1.models import AccessRecord, Topic, Webpage 

fake_gen = Faker()

def give_topic():

    topics_list = ['E-Commerce', 'Social Networking', 'Docs', 'News', 'Food', 'Games', 'Private']

    topic_name = random.choice(topics_list)
    topic = Topic.objects.get_or_create(topic_name=topic_name)[0]

    return topic

def populate_db(N = 10):
    
    for i in range(N):
        fake_topic = give_topic()
        fake_url = fake_gen.url()
        fake_name = fake_gen.company()

        fake_date = fake_gen.date()

        webpage = Webpage.objects.get_or_create(topic=fake_topic, name=fake_name, url=fake_url)[0]

        access_record = AccessRecord.objects.gWet_or_create(webpage=webpage, last_access=fake_date)[0]

if __name__ == "__main__":
    print('Starting to populate')
    populate_db(20)
    print('Finished!')
    

