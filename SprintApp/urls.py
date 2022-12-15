from django import views
from SprintApp import views
from django.urls import path

urlpatterns=[
    path('/<int:sprint_id>',views.sprinttApi),

    path(r'^feature$',views.featureApi),
    path(r'^feature/([0-9]+)$',views.featureApi),

    path(r'^tache$',views.tacheApi),
    path(r'^tache/([0-9]+)$',views.tacheApi)


]

