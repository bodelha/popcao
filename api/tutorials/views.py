import json
from django.db.models.query import InstanceCheckMeta
from django.http import response
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import Breed, Tutor, Pet, Service, ServiceOrder
from tutorials.serializers import  *
from rest_framework.decorators import api_view


@api_view(['GET'])
def settings(request):
    if request.method == 'GET':
        services = Service.objects.all()
        service_serializer = SettingsSerializer(services, many=True)
        return JsonResponse(service_serializer.data, safe=False)


@api_view(['GET'])
def services(request):
    if request.method =='GET':
        services = Service.objects.all()
        service_serializer = ServiceSerializer(services, many=True)
        return JsonResponse(service_serializer.data, safe=False)


@api_view(['PUT', 'GET', 'POST', 'DELETE'])
def service(request, pk=None):
    service, created =Service.objects.get_or_create(pk=pk)
    print(request, pk, '\n', service, created)
    if created and request.method =='PUT':
        service_data = JSONParser().parse(request)
        service_serializer = ServiceSerializer(data=service_data)
        if service_serializer.is_valid():
            service_serializer.save()
            return JsonResponse(service_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif not created and request.method == 'POST':
        try:
            service_data = JSONParser().parse(request)
            service_serializer = ServiceSerializer(data=service_data)
            if service_serializer.is_valid():
                service_serializer.update(
                    Service(service.id_service),
                    service_serializer.validated_data
                )
                return JsonResponse(service_serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return JsonResponse(service_serializer.data, status=status.HTTP_304_NOT_MODIFIED)
        except ServiceSerializer.errors:
            return JsonResponse(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        service_serializer = ServiceSerializer(service)
        return JsonResponse(service_serializer.data)
        
    elif request. method == 'DELETE':
        service.delete()
        return JsonResponse({'message': 'Service was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST', 'DELETE'])
# def tutorial_list(request):
#     if request.method == 'GET':
#         tutorials = Tutorial.objects.all()
        
#         title = request.GET.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
        
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#         # 'safe=False' for objects serialization
 
#     elif request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         count = Tutorial.objects.all().delete()
#         return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     try: 
#         tutorial = Tutorial.objects.get(pk=pk) 
#     except Tutorial.DoesNotExist: 
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
#     if request.method == 'GET': 
#         tutorial_serializer = TutorialSerializer(tutorial) 
#         return JsonResponse(tutorial_serializer.data) 
 
#     elif request.method == 'PUT': 
#         tutorial_data = JSONParser().parse(request) 
#         tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
#         if tutorial_serializer.is_valid(): 
#             tutorial_serializer.save() 
#             return JsonResponse(tutorial_serializer.data) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
#     elif request.method == 'DELETE': 
#         tutorial.delete() 
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
# @api_view(['GET'])
# def tutorial_list_published(request):
#     tutorials = Tutorial.objects.filter(published=True)
        
#     if request.method == 'GET': 
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
    
