# from typing_extensions import Required
from functools import partial
from django.db.models import fields
from django.utils import tree
from rest_framework import serializers 
from tutorials.models import *


class BreedSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Breed
        fields = (
            'id_breed',
            'name_breed',
            'groomable',
        )

class BreedDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = (
            'id_breed',
            'name_breed',
            'groomable',
            'set'
        )

class SettingsSerializer(serializers.ModelSerializer):
    breeds = BreedSerializer(source='set', many=True)

    class Meta:
        model = Service
        fields = (
            'id_service',
            'breeds',
            'name_service',
            'time_service',
            'short_fur',
            'medium_fur',
            'long_fur',
        )
        depth=1

    def create(self, validated_data):
        breed_data = validated_data.pop('set')
        service = Service.objects.create(**validated_data)
        for _breed in breed_data:
            breed = Breed.objects.create(**_breed)
            Group.objects.create(
                id_service = service,
                breed = breed
            )
        return service.id_service

    def update(self, instance, data):
        breed_data = data.pop('set')
        service_data = SettingsSerializer(data=data, partial=True)
        if service_data.is_valid():
            service = Service.objects.update(**service_data.validated_data)
            instance.set.clear()
            for _breed in breed_data:
                breed_ = BreedSerializer(data=_breed)
                if breed_.is_valid():
                    if "id_breed" in breed_.initial_data:
                        breed_obj = Breed.objects.filter(pk=breed_.initial_data['id_breed'])
                        breed_obj.update(**breed_.data)
                        Group.objects.update_or_create(
                            id_service = instance,
                            breed = breed_obj.first()
                        )
                    else:
                        breed_obj = Breed.objects.create(**breed_.validated_data)
                        Group.objects.update_or_create(
                            id_service = instance,
                            breed = breed_obj
                        )
            return service

    
class ServiceSerializer(serializers.ModelSerializer):
    breeds = BreedSerializer(source='set', many=True)

    class Meta:
        model = Service
        fields = (
            'id_service',
            'breeds',
            'name_service',
            'time_service',
            'short_fur',
            'medium_fur',
            'long_fur',
        )

class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = (
            'id_pet',
            'breed_id',
            'name_pet',
        )

class PetDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = (
            'id_pet',
            'name_pet',
            'breed_id',
            'id_tutor',
            'puppy',
            'sex'
        )

class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = (
            'id_tutor',
            'name_tutor',
            'cellphone1',
            'cellphone2',
            'endereco_tutor',
        )

class TutorDetailSerializer(serializers.ModelSerializer):
    pets=PetDetailSerializer(source='pets_set', many=True)

    class Meta:
        model = Tutor
        fields = (
            'id_tutor',
            'name_tutor',
            'cellphone1',
            'cellphone2',
            'endereco_tutor',
            'pets'
        )
    
    def create(self, validated_data):
        pets = validated_data.pop('pets_set')
        tutor = Tutor.objects.create(**validated_data)
        for _pet in pets:
            _pet["id_tutor"] = tutor
            Pet.objects.create(**_pet)
        return tutor.id_tutor

    def update(self, instance, data):
        pets_data = data.pop('pets_set')
        new_pets=[]
        tutor_data = TutorDetailSerializer(data=data, partial=True)
        if tutor_data.is_valid():
            tutor_obj = Tutor.objects.filter(pk=instance.id_tutor)
            tutor_obj.update(**tutor_data.validated_data)
            for _pet in pets_data:
                pet_ = PetDetailSerializer(data=_pet)
                if pet_.is_valid():
                    if 'id_pet' in pet_.initial_data:
                        pet_obj=Pet.objects.filter(pk=pet_.initial_data['id_pet'])
                        pet_obj.update(**pet_.data)
                        new_pets.append(pet_obj.first())
                    else:
                        _pet["id_tutor"] = instance.id_tutor
                        pet = PetDetailSerializer(data=_pet, partial=True)
                        if pet.is_valid():
                            pet_obj = Pet.objects.create(**pet.validated_data)
                            new_pets.append(pet_obj)
            return tutor_obj

class AttendanceSerializer(serializers.ModelSerializer):
    # service_order =ServiceOrderSerializer(source='id_attendance')
    pet_id = PetSerializer()
    service_category=ServiceSerializer()

    class Meta:
        model = Attendance
        fields = (
            # 'service_order',
            'pet_id',
            'service_category',
            'service_duration',
            'observation'
        )

class ServiceOrderSerializer(serializers.ModelSerializer):
    attendances=AttendanceSerializer(source='attendances_set', many=True)

    class Meta:
        model = ServiceOrder
        fields = (
            'id_order',
            'tutor_id',
            'pet_ids', 
            'attendances'
        )
    def create(self, validated_data):
        pets = validated_data.pop('pets_set')
        tutor = Tutor.objects.create(**validated_data)
        for _pet in pets:
            _pet["id_tutor"] = tutor
            Pet.objects.create(**_pet)
        return tutor.id_tutor

    def update(self, instance, data):
        pets_data = data.pop('pets_set')
        new_pets=[]
        tutor_data = TutorDetailSerializer(data=data, partial=True)
        if tutor_data.is_valid():
            tutor_obj = Tutor.objects.filter(pk=instance.id_tutor)
            tutor_obj.update(**tutor_data.validated_data)
            for _pet in pets_data:
                pet_ = PetDetailSerializer(data=_pet)
                if pet_.is_valid():
                    if 'id_pet' in pet_.initial_data:
                        pet_obj=Pet.objects.filter(pk=pet_.initial_data['id_pet'])
                        pet_obj.update(**pet_.data)
                        new_pets.append(pet_obj.first())
                    else:
                        _pet["id_tutor"] = instance.id_tutor
                        pet = PetDetailSerializer(data=_pet, partial=True)
                        if pet.is_valid():
                            pet_obj = Pet.objects.create(**pet.validated_data)
                            new_pets.append(pet_obj)
            return tutor_obj

