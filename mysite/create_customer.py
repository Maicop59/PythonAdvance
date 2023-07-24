import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from pagination.models import Customer

Customer.objects.create(name = 'Alfreds Futterkiste', country='Germany')
Customer.objects.create(name = 'Ronaldo Derlima', country='Brazil')
Customer.objects.create(name = 'Saka', country='England')
Customer.objects.create(name = 'Ozil', country='Germany')
Customer.objects.create(name = 'Kaka', country='Brazil')
Customer.objects.create(name = 'Henry', country='France')
Customer.objects.create(name = 'Mitoma', country='Janpan')
Customer.objects.create(name = 'Casilas', country='Spain')
Customer.objects.create(name = 'Balogun', country='UK')
Customer.objects.create(name = 'Buffon', country='Italia')
Customer.objects.create(name = 'Ibrahimovic', country='Sweden')
Customer.objects.create(name = 'Ashavin', country='Rusia')