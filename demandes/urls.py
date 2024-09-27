from django.urls import path

from demandes.views import create_demande_api

urlpatterns = [
    path('api/create-demande/', create_demande_api, name='create_demande_api'),
]
