from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("ex", views.frontend, name = "frontend"),
    path("frontend2", views.frontend2, name = "frontend2"),
    path("samson", views.samson, name = "samson"),

]
#views.index tells us when we hit this path (root path) go to views and call the index function
