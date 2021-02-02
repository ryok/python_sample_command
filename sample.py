import csv
import random
from faker import Faker
from faker.providers import profile

fake = Faker('ja_JP')
fake.add_provider(profile)
with open('./fake_data.csv', 'w') as f:
    writer = csv.writer(f)
    for _ in range(100):
        writer.writerow([fake.name(), random.randint(18, 75),
                         "男性" if fake.simple_profile()['sex'] == 'M' else "女性",
                        fake.address(), fake.job()])