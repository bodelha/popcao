from django.db import models
from django.db.models import fields
from rest_framework import serializers 
# from tutorials.models import Service, Tutorial
from tutorials.models import Service, Tutor, Pet
 
 
# class TutorialSerializer(serializers.ModelSerializer):
 
#     class Meta:
#         model = Tutorial
#         fields = ('id',
#                   'title',
#                   'description',
#                   'published')


class ServiceSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Service
        fields = ('name_service',
                  'small_time',
                  'medium_time',
                  'large_time')


class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = (
            'name_tutor',
            'cellphone_tutor'
        )

        
class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = (
            'name_pet'
            'tutor_pet'
        )