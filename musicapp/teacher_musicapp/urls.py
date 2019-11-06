from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index") 
]
#views.index tells us when we hit this path (root path) go to views and call the index function
