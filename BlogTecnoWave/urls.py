"""
URL configuration for Proyectocoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from BlogTecnoWave.views import *


urlpatterns = [
    path("", inicio, name='Inicio'),
    path("busqueda-profile/", busqueda_profile, name="BusquedaProfile"),
    path("buscar-profile", buscar_profile, name="BuscarProfile"),
    path("users-list/", lista_users , name="UsersList"),
    path("user-create/", userCreate.as_view() , name="UserCreate"),
    path("profiles-list/", lista_profiles , name="ProfilesList"),
    path("profile-create/", profileCreate.as_view() , name="ProfileCreate"),
    path("entries-list/", lista_entries , name="EntriesList"),
    path("entry-create/", entryCreate.as_view() , name="EntryCreate"),

]
