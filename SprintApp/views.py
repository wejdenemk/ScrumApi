from symbol import decorators
from django.shortcuts import render
from django.urls import is_valid_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

from SprintApp.models import Sprints,Features,Taches
from SprintApp.serializers import SprintSerializer,FeatureSerializer,TacheSerializer


@csrf_exempt
def sprintApi(request,id=0):
    if request.method=='GET':
        sprints = Sprints.objects.all()
        sprints_serializer = SprintSerializer(sprints,many=True)
        return JsonResponse(sprints_serializer.data, safe = False)
    elif request.method == 'POST':
        sprint_data=JSONParser().parse(request)
        sprints_serializer=SprintSerializer(data=sprint_data)
        if sprints_serializer.is_valid():
            sprints_serializer.save()
            return JsonResponse("Added Successfully",safe = False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        sprint_data=JSONParser().parse(request)
        sprint=Sprints.objects.get(SprintId=sprint_data['SprintId'])
        sprints_serializer=SprintSerializer(sprint,data=sprint_data)
        if sprints_serializer.is_valid():
            sprints_serializer.save()
            return JsonResponse("Update Successfully", safe=  False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        sprint=Sprints.objects.get(SprintId=id)
        sprint.delete()
        return JsonResponse("Delete Successfully",safe=False)


@csrf_exempt
def sprinttApi(request,id=0):
    if request.method=='DELETE':
        sprint=Sprints.objects.get(SprintId=id)
        sprint.delete()
        return JsonResponse("Delete Successfully",safe=False)


@csrf_exempt
def featureApi(request,id=0):
    if request.method=='GET':
        features = Features.objects.all()
        features_serializer = FeatureSerializer(features,many=True)
        return JsonResponse(features_serializer.data, safe = False)
    elif request.method == 'POST':
        feature_data=JSONParser().parse(request)
        features_serializer=FeatureSerializer(data=feature_data)
        if features_serializer.is_valid():
            features_serializer.save()
            return JsonResponse("Added Successfully",safe = False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        feature_data=JSONParser().parse(request)
        feature=Features.objects.get(FeatureId=feature_data['FeatureId'])
        features_serializer=FeatureSerializer(feature,data=feature_data)
        if features_serializer.is_valid():
            features_serializer.save()
            return JsonResponse("Update Successfully", safe=  False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        feature_data=JSONParser().parse(request)
        feature=Features.objects.get(FeatureId=feature_data['FeatureId'])
        feature.delete()
        return JsonResponse("Delete Successfully",safe=False)


@csrf_exempt
def tacheApi(request,id=0):
    if request.method=='GET':
        taches = Taches.objects.all()
        taches_serializer = TacheSerializer(taches,many=True)
        return JsonResponse(taches_serializer.data, safe = False)
    elif request.method == 'POST':
        tache_data=JSONParser().parse(request)
        taches_serializer=TacheSerializer(data=tache_data)
        if taches_serializer.is_valid():
            taches_serializer.save()
            return JsonResponse("Added Successfully",safe = False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        tache_data=JSONParser().parse(request)
        tache=Taches.objects.get(TacheId=tache_data['TacheId'])
        taches_serializer=TacheSerializer(tache,data=tache_data)
        if taches_serializer.is_valid():
            taches_serializer.save()
            return JsonResponse("Update Successfully", safe=  False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        tache_data=JSONParser().parse(request)
        tache=Taches.objects.get(TacheId=tache_data['TacheId'])
        tache.delete()
        return JsonResponse("Delete Successfully",safe=False)


