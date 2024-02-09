from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name='Index'),
    path("country", views.country, name='Country')
]