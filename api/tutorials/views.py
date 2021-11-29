from functools import partial
import json
from django.db.models.query import InstanceCheckMeta
from django.http import response
from django.shortcuts import render

from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
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

@api_view(['POST'])
def create_service(request):
    if request.method =='POST':
        service_data = JSONParser().parse(request)
        service_serializer = SettingsSerializer(data=service_data)
        if service_serializer.is_valid():
            service = service_serializer.create(service_serializer.validated_data)
            return JsonResponse(SettingsSerializer(Service(service)).data, status=status.HTTP_201_CREATED) 
        return JsonResponse(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'GET', 'DELETE'])
def service(request, pk=None):
    try:
        service = Service.objects.get(pk=pk)
    # print(request, pk, '\n', service)
        if request.method == 'PUT':
            try:
                service_data = JSONParser().parse(request)
                service_serializer = SettingsSerializer(service, data=service_data, partial=True)
                if service_serializer.is_valid():
                    service_serializer.update(instance=service, data=service_serializer.initial_data)
                    return JsonResponse(service_serializer.data, status=status.HTTP_202_ACCEPTED)
                else:
                    return JsonResponse(service_serializer.data, status=status.HTTP_304_NOT_MODIFIED)
            except SettingsSerializer.errors:
                return JsonResponse(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET'and service:
            service_serializer = SettingsSerializer(service)
            return JsonResponse(service_serializer.data)
            
        elif request. method == 'DELETE':
            service.delete()
            return JsonResponse({'message': 'Service was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'Service not exists!'}, status=status.HTTP_410_GONE)
    except Exception as e:
        return e

@api_view(['GET'])
def breeds(request):
    if request.method == 'GET':
        breeds = Breed.objects.all()
        serializer = BreedDetailSerializer(breeds, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def create_breed(request):
    if request.method =='POST':
        breed_data = JSONParser().parse(request)
        breed_serializer = BreedDetailSerializer(data=breed_data)
        if breed_serializer.is_valid():
            breed_serializer.create(breed_serializer.validated_data)
            return JsonResponse(breed_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(breed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def breed_detail(request, pk):
    breed =Breed.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = BreedDetailSerializer(breed)
        return JsonResponse(serializer.data)

@api_view(['GET'])
def tutors(request):
    if request.method == 'GET':
        tutors =  Tutor.objects.all()
        serializer = TutorDetailSerializer(tutors, many=True)
        return JsonResponse(serializer.data, safe=False)
        
@api_view(['PUT', 'GET', 'DELETE'])
def tutor_detail(request, pk):
    try:
        tutor = Tutor.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = TutorDetailSerializer(tutor)
            return JsonResponse(serializer.data, safe=False)
        elif request.method == "PUT":
            try:
                tutor_data = JSONParser().parse(request)
                tutor_serializer = TutorDetailSerializer(tutor, data=tutor_data, partial=True)
                if tutor_serializer.is_valid():
                    tutor_serializer.update(instance=tutor, data=tutor_serializer.initial_data)
                    return JsonResponse(tutor_serializer.data, status=status.HTTP_202_ACCEPTED)
                else:
                    return JsonResponse(tutor_serializer.data, status=status.HTTP_304_NOT_MODIFIED)
            except SettingsSerializer.errors:
                return JsonResponse(tutor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE":
            tutor.delete()
            return JsonResponse({'message': 'Tutor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'Service not exists!'}, status=status.HTTP_410_GONE)
    except Exception as e:
        return e


@api_view(['GET'])
def schedule(request):
    if request.method == 'GET':
        orders = ServiceOrder.objects.all()
        serializer = ServiceOrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def pets(request):
    if request.method == 'GET':
        pets =  Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def create_tutor(request):
    if request.method =='POST':
        tutor_data = JSONParser().parse(request)
        tutor_serializer = TutorDetailSerializer(data=tutor_data)
        if tutor_serializer.is_valid():
            tutor = tutor_serializer.create(tutor_serializer.validated_data)
            return JsonResponse(TutorDetailSerializer(Tutor(tutor)).data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def order(request):
    if request.method =='POST':
        order_data = JSONParser().parse(request)
        serializer = ServiceOrderSerializer(data=order_data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_detail(request, pk):
    order =ServiceOrder.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ServiceOrderSerializer(order)
        return JsonResponse(serializer.data)

# @api_view(['GET'])
# def services(request):
#     if request.method =='GET':
#         services = Service.objects.all()
#         service_serializer = ServiceSerializer(services, many=True)
#         return JsonResponse(service_serializer.data, safe=False)
# 
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
    
