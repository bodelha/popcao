from django.db import models
from datetime import timedelta
from django.db.models.deletion import CASCADE

from django.db.models.fields.related import ForeignKey
# from api.tutorials.views import services


class Breed(models.Model):
    id_breed = models.BigAutoField(verbose_name='Id', primary_key=True, db_column='Id')
    name_breed = models.CharField(verbose_name='Raça', max_length=50, db_column='Raca')
    groomable = models.BooleanField(verbose_name='Tosa Estética', default=False, db_column='TosaEstetica')
    last_update = models.DateTimeField(auto_now=True, db_column='LastUpdate')

class Service(models.Model):
    id_service = models.BigAutoField(primary_key=True, db_column='Id')
    breeds_set = models.ManyToManyField(to=Breed, through='Group')
    name_service = models.CharField(max_length=80, verbose_name='Nome Serviço', db_column='NomeServico')
    time_service = models.DurationField(blank=True, null=True, db_column='TempoMedioGrupoRaca')
    short_fur = models.DurationField(blank=True, null=True, db_column='TempoMedioPeloCurto')
    medium_fur = models.DurationField(blank=True, null=True, db_column='TempoMedioPeloMedio')
    long_fur = models.DurationField(blank=True, null=True, db_column='TempoMedioPeloLongo')
    last_update = models.DateTimeField(auto_now=True, db_column='LastUpdate')

class Group(models.Model):
    breed = models.ForeignKey(to=Breed, on_delete=models.CASCADE)
    id_service = models.ForeignKey(to=Service, on_delete=CASCADE)

class Tutor(models.Model):
    id_tutor = models.BigAutoField(primary_key=True, db_column='Id', default=42)
    name_tutor = models.CharField(max_length=50, blank=False)
    cellphone1 = models.IntegerField(verbose_name="Telefone Principal", db_column='Telefone1', default=-1)
    cellphone2 = models.IntegerField(verbose_name="Outro Telefone", null=True, db_column='Telefone2', blank=True)
    endereco_tutor = models.CharField(max_length=300, blank=True)
    last_update = models.DateTimeField(auto_now=True, db_column='LastUpdate')

class Pet(models.Model):
    SEX_CHOICES = (
        ('M', 'Macho'),
        ('F', 'Fêmea'),
        ('D', 'Desconhecido'),
    )
    id_pet = models.AutoField(verbose_name='PetId', primary_key=True, db_column='Id')
    name_pet = models.CharField(max_length=50, blank=False, default='n', db_column='Nome')
    breed_id = models.ForeignKey(to=Breed, on_delete=models.CASCADE, db_column='RacaId', default=-1)
    tutor_id = models.ForeignKey(to=Tutor, on_delete=models.CASCADE, db_column='TutorId', default= -1)
    puppy = models.BooleanField(verbose_name='Filhote', default=False, db_column='Filhote')
    sex = models.CharField(max_length=1, verbose_name='Sexo', db_column='Sexo', choices=SEX_CHOICES, default='D')
    last_update = models.DateTimeField(auto_now=True, db_column='LastUpdate')

class ServiceOrder(models.Model):
    id_attendance = models.BigAutoField(primary_key=True, db_column='Id')
    tutor_id = models.ForeignKey(to=Tutor, on_delete=models.CASCADE, db_column='TutorId')
    pet_ids = models.ManyToManyField(to=Pet, through='Attendance')
    date = models.DateTimeField(auto_now=True)

class Attendance(models.Model):
    service_order = models.ForeignKey(to=ServiceOrder, on_delete=models.CASCADE)
    pet_id = models.ForeignKey(to=Pet, on_delete=models.CASCADE)