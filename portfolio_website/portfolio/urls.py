from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("Home", views.Home, name="Home"),
    path("About", views.About, name="About"),
    path("Contact", views.Contact, name="Contact")
]