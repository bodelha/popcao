from tutorials.models import *
from datetime import timedelta
from django.db import connection


connection.connect()


shi = Breed()
shi.name_breed = 'Shih-tzu'
shi.groomable = True
shi.save()

lhasa = Breed()
lhasa.name_breed = 'Lhasa Apso'
lhasa.groomable = True
lhasa.save()

york = Breed()
york.name_breed = 'Yorkshire'
york.groomable = True
york.save()

malt = Breed()
malt.name_breed = 'Maltês'
malt.groomable = True
malt.save()

spitz = Breed()
spitz.name_breed = 'Spitz'
spitz.groomable = True
spitz.save()

s1 = Service()
s1.name_service = "Banho + Tosa Higiênica G1"
s1.short_fur = timedelta(minutes=36)
s1.medium_fur = timedelta(minutes=42)
s1.long_fur = timedelta(minutes=54)
s1.save()

for i in (shi, lhasa, york, malt, spitz):
    r = Group(breed=i, id_service=s1)
    r.save()


pinscher = Breed()
pinscher.name_breed= 'Pinscher'
pinscher.save()

fox = Breed()
fox.name_breed= 'Fox Paulistinha'
fox.save()

dash = Breed()
dash.name_breed= 'Dachshund'
dash.save()

pug = Breed()
pug.name_breed= 'Pug'
pug.save()

s2 = Service()
s2.name_service = "Banho + Tosa Higiênica G3"
s2.time_service = timedelta(minutes=30)
s2.save()

for i in (pinscher, fox, dash, pug):
    r = Group(breed=i, id_service=s2)
    r.save()

tutor = Tutor()
tutor.name_tutor = 'João'
tutor.cellphone1 = '9999999999'
tutor.save()

p1 = Pet()
p1.name_pet = 'Pantera'
p1.breed_id= pug
p1.puppy=False
p1.sex = 'M'
p1.id_tutor=tutor
p1.save()

p2 = Pet()
p2.name_pet = 'Cacau'
p2.breed_id= malt
p2.puppy=True
p2.sex = 'F'
p2.id_tutor=tutor
p2.save()

p3 = Pet()
p3.name_pet = 'Mingau'
p3.breed_id= york
p3.puppy=False
p3.sex = 'M'
p3.id_tutor=tutor
p3.save()



o1 = ServiceOrder()
o1.tutor_id=tutor
o1.save()

a1 = Attendance()
a1.id_order=o1
a1.pet_id = p1
a1.service_category = p1.breed_id.set.first()
a1.service_duration = 1.2*a1.service_category.time_service
a1.observation = "Alergia ao xampu xpto"
a1.save()


a2 = Attendance()
a2.id_order=o1
a2.pet_id = p2
a2.service_category = p2.breed_id.set.first()
a2.service_duration = 0.9*a2.service_category.short_fur
a2.save()

a3 = Attendance()
a3.id_order=o1
a3.pet_id = p3
a3.service_category = p3.breed_id.set.first()
a3.service_duration = 1.5*a3.service_category.long_fur
a3.save()