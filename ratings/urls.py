from django.urls import path
from . import views

urlpatterns =[
    path("",views.index),
    path("addyourprofessors",views.add,name="add"),
    path("ratingstheperson",views.prof,name="rating")
]