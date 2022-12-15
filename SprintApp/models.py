from django.db import models

# Create your models here.
class Sprints(models.Model):
    SprintId = models.AutoField(primary_key=True)
    SprintName = models.CharField(max_length=10)
    SprintDuration = models.CharField(max_length=10)

class Features(models.Model):
    FeatureId = models.AutoField(primary_key=True)
    FeatureName = models.CharField(max_length=10)
    FeaturePriority = models.IntegerField(default=0)
    FeatureSprint = models.ForeignKey(Sprints, on_delete=models.CASCADE)

class Taches(models.Model):
    TacheId = models.AutoField(primary_key=True)
    TacheName = models.CharField(max_length=10)
    TacheStoryPoint = models.IntegerField()
    TacheProgress = models.IntegerField(default=0)
    TacheFeature = models.ForeignKey(Features, on_delete=models.CASCADE)

