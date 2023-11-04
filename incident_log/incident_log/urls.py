"""
URL configuration for incident_log project.

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
from django.contrib import admin
from django.urls import path
from incident.views import (get_all_incidents,get_all_incidents_type,
                            create_incident,search_by_incident_type,search_incidents_from_to,create_type)

urlpatterns = [
    path("api/incident//", get_all_incidents, name="get-all-incidents"),
    path("api/incident_type//", get_all_incidents_type, name="get-all-incident-types"),
]