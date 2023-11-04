from rest_framework import serializers
from .models import Incident, IncidentType


class IncidentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentType
        fields = ('id', 'name')


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('id', 'incident_type', 'comment', 'create_time', 'open_incident_time', 'close_incident_time', 'acknowledge_time')