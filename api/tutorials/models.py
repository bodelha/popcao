from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE

# from api.tutorials.views import services



class Service(models.Model):
    id_service = models.BigAutoField(primary_key=True, db_column='Id')
    set = models.ManyToManyField(to='Breed', through='Group')
    name_service = models.CharField(max_length=80, verbose_name='Nome Serviço', db_column='NomeServico')
    time_service = models.DurationField(blank=True, null=True, db_column='TempoMedioGrupoRaca')
    short_fur = models.DurationField(blank=True, null=True, db_column='TempoMedioPeloCurto')
    medium_fur = models.DurationField(blank=True, null=True, db_column='TempoMedioPeloMedio')
    long_fur = models.DurationField(blank=True, null=True, db_column='TempoMedioPeloLongo')
    last_update = models.DateTimeField(auto_now=True, db_column='LastUpdate')

class Breed(models.Model):
    id_breed = models.BigAutoField(verbose_name='Id', primary_key=True, db_column='Id')
    name_breed = models.CharField(verbose_name='Raça', max_length=50, db_column='Raca')
    groomable = models.BooleanField(verbose_name='Tosa Estética', default=False, db_column='TosaEstetica')
    set = models.ManyToManyField(to='Service', through='Group')
    last_update = models.DateTimeField(auto_now=True, db_column='LastUpdate')

class Group(models.Model):
    breed = models.ForeignKey(to=Breed, on_delete=models.CASCADE)
    id_service = models.ForeignKey(to=Service, on_delete=CASCADE)

class Tutor(models.Model):
    id_tutor = models.BigAutoField(primary_key=True, db_column='Id', default=42)
    name_tutor = models.CharField(max_length=50, blank=False)
    cellphone1 = models.CharField(max_length=15, verbose_name="Telefone Principal", db_column='Telefone1', default='-1')
    cellphone2 = models.CharField(max_length=15, verbose_name="Outro Telefone", null=True, db_column='Telefone2', blank=True)
    endereco_tutor = models.CharField(max_length=300, blank=True)
    pets_set = models.ManyToOneRel(field_name='id_tutor', to='Pet', field='id_tutor')
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
    id_tutor = models.ForeignKey(to=Tutor, related_name='pets_set', on_delete=models.CASCADE, db_column='TutorId', default= -1)
    puppy = models.BooleanField(verbose_name='Filhote', default=False, db_column='Filhote')
    sex = models.CharField(max_length=1, verbose_name='Sexo', db_column='Sexo', choices=SEX_CHOICES, default='D')
    last_update = models.DateTimeField(auto_now=True, db_column='LastUpdate')

class ServiceOrder(models.Model):
    id_order = models.BigAutoField(primary_key=True, db_column='Id')
    attendances_set = models.ManyToOneRel(to='Attendance', field_name='id_order', field='service_order')
    tutor_id = models.ForeignKey(to=Tutor, on_delete=models.CASCADE, db_column='TutorId')
    pet_ids = models.ManyToManyField(to=Pet, through='Attendance')
    creation = models.DateTimeField(auto_now_add=True, db_column='CreationTime')
    last_update = models.DateTimeField(auto_now=True, db_column='LastUpdate')

class Attendance(models.Model):
    id_attendance = models.BigAutoField(primary_key=True, db_column='Id')
    id_order = models.ForeignKey(to=ServiceOrder, related_name='attendances_set', on_delete=models.CASCADE, db_column='ServiceOrderFK')
    pet_id = models.ForeignKey(to=Pet, on_delete=models.CASCADE)
    service_category = models.ForeignKey(to=Service, on_delete=models.CASCADE)
    service_duration = models.DurationField(db_column='DuracaoServico')
    observation = models.CharField(max_length=300, blank=True, db_column='Observacao')