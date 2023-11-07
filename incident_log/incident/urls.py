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
from incident.views import (search_by_description,search_incidents_from_to, create_incident,create_type_incident,search_incidents_by_type_id,
                            get_all,search_incidents_from_to,search_by_description, IncidentList,IncidentTypeList,IncidentTypeDetail,IncidentDetail)
urlpatterns = [
    path("api//", get_all, name="get-all"),
    path("api/incident_type//create", create_type_incident, name='create-incident-type'),
    path("api/incident//create", create_incident, name='create-incident'),
    path("api/incident_type/", IncidentTypeList.as_view(), name="incident-type-list"),
    path("api/incident/", IncidentList.as_view(), name="incident-list"),
    path("api/incident/<uuid:pk>", IncidentDetail.as_view(), name='incident-detail'),
    path("api/incident_type/<uuid:pk>", IncidentTypeDetail.as_view(), name='incident-type-detail'),
    path("api/incident/search/by-date",search_incidents_from_to,name='search-by-date'),
    path("api/incident/search/by-description",search_by_description, name='search-by-description'),
    path("api/incident/search/by-type-id", search_incidents_by_type_id, name='search-type-id')

]