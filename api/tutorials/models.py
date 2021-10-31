from django.db import models


# class Tutorial(models.Model):
#     title = models.CharField(max_length=70, blank=False, default='')
#     description = models.CharField(max_length=200,blank=False, default='')
#     published = models.BooleanField(default=False)


class Service(models.Model):
    id_service = models.BigAutoField(verbose_name='ServiceId', primary_key=True)
    name_service = models.CharField(verbose_name='nameService', max_length=70, blank=False, default="0:30:00")
    small_time = models.DurationField(verbose_name='smallTime', blank=False, default="0:30:00")
    medium_time = models.DurationField(verbose_name='mediumTime', blank=False, default="0:35:00")
    large_time = models.DurationField(verbose_name='largeTime', blank=False, default="0:40:00")

class Tutor(models.Model):
    cellphone_tutor = models.IntegerField(primary_key=True)
    name_tutor = models.CharField(max_length=50, blank=False)
    # pet_tutor = models.ForeignObject(to=Pet)

class Pet(models.Model):
    id_pet = models.AutoField(verbose_name='PetId', primary_key=True)
    name_pet = models.CharField(max_length=50, blank=False, default='n')
    tutor_pet = models.ForeignKey(to=Tutor, on_delete=models.CASCADE)