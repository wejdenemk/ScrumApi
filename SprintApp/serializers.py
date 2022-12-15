from dataclasses import fields
from rest_framework import serializers
from SprintApp.models import Sprints,Features,Taches

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprints
        fields=('SprintId', 'SprintDuration','SprintName')

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields= ('FeatureId','FeatureName','FeaturePriority','FeatureSprint' )

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taches
        fields= ('TacheId','TacheName','TacheStoryPoint','TacheProgress','TacheFeature')
