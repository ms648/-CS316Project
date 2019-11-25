from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("frontend", views.frontend, name = "frontend")
]
#views.index tells us when we hit this path (root path) go to views and call the index function
