from faker import Faker
from django.core.management.base import BaseCommand

import random
from datetime import datetime

from blog.models import Post,Category
from account.models import User,Profile

cat_list = [
    "IT",
    "Programmer",
    "Python",
    "Backend",
    "Django",
    "Developer"
]

class Command(BaseCommand) :
    help = "inserting dummy data"

    def __init__(self,*args,**kwargs):
        super(Command,self).__init__(*args,**kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(),password="Mm20399990")
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()

        for name in cat_list :
            Category.objects.get_or_create(name=name)

        for _ in range(10) :
            Post.objects.create(
                title = self.fake.paragraph(nb_sentences=1),
                content = self.fake.paragraph(nb_sentences=2),
                author = user,
                category = Category.objects.get(name=random.choice(cat_list)),
                status = True,
                published_date = datetime.now()

            )