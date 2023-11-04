from rest_framework import serializers
from .models import Incident, IncidentType


class IncidentTypeSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        return IncidentType.objects.create(**validated_data)
    class Meta:
        model = IncidentType
        fields = ('id', 'name','style')


class IncidentSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return Incident.objects.create(**validated_data)
    class Meta:
        model = Incident
        fields = ('__all__')