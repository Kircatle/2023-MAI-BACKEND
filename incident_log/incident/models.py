from django.db import models
import uuid

from datetime import datetime

from django.db import models

class IncidentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False, max_length=128, blank=False,unique=True)
    style = models.TextField(null=True, max_length=128, blank=False)

    def __str__(self):
        return str(self.name) + " (" + str(self.id) + ")"

    class Meta:
        ordering = ["name"]
        verbose_name = "Incident type"
        verbose_name_plural = "Incident types"
        db_table = "incident_type"

    def to_json(self):
        return {
            "id": str(self.id),
            "name": str(self.name),
            "style": self.style if self.style is not None else None,
        }
    
class Incident(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    incident_type = models.ForeignKey(IncidentType, on_delete=models.SET_NULL, verbose_name='Incident type', null=True)
    description = models.CharField(max_length=1024, verbose_name='Description', null=True, unique=False)
    create_time = models.DateTimeField(verbose_name='Create time', default=datetime.now)
    open_incident_time = models.DateTimeField(verbose_name='Open time', default=datetime.now)
    close_incident_time = models.DateTimeField(verbose_name='Close time',null=True,default=None)
    acknowledge_time = models.DateTimeField(verbose_name='Acknowledge time',null=True,default=None)

    def __str__(self):
        return f"Incident: {self.incident_type.name} ({self.id})"

    class Meta:
        verbose_name = "Incident"
        verbose_name_plural = "Incidents"
        ordering = ('open_incident_time','create_time')
        db_table = "incident"
    
    def to_json(self):
        return {
            "id": str(self.id),
            "incident_type_id": self.incident_type.id if self.incident_type is not None else None,
            "description": self.description,
            "create_time": str(self.create_time),
            "open_incident_time": str(self.open_incident_time),
            "close_incident_time": str(self.close_incident_time) if self.close_incident_time is not None else None,
            "acknowledge_time": str(self.acknowledge_time) if self.acknowledge_time is not None else None,
        }