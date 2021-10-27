from rest_framework import serializers 
from tutorials.models import Service, Tutorial
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')


class ServicesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Service
        fields = ('nameService',
                  'smallTime',
                  'mediumTime',
                  'largeTime')
