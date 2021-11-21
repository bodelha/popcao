from rest_framework import serializers 
from tutorials.models import Service, Breed, Tutor, Pet, ServiceOrder


class BreedSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Breed
        fields = (
            'id_breed',
            'name_breed',
            'groomable'
        )

class SettingsSerializer(serializers.ModelSerializer):
    breeds = BreedSerializer(source='breeds_set', many=True)

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
    
class ServiceSerializer(serializers.ModelSerializer):
    breeds = BreedSerializer()

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

class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = (
            'id_tutor',
            'name_tutor',
            'cellphone1',
            'cellphone2',
            'cellphone3',
            'endereco_tutor'
        )

        
class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = (
            'id_pet',
            'name_pet',
            'breed_id',
            'tutor_id',
            'puppy',
            'sex'
        )

class ServiceOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceOrder
        fields = (
            'id_attendance',
            'tutor_id',
            'pet_ids'
        )
