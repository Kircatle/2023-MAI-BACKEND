from django.shortcuts import render

import json

from django.core.handlers.asgi import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import IncidentType, Incident

@csrf_exempt
@require_http_methods(["GET"])
def search_by_description(request: HttpRequest) -> JsonResponse:
    description = request.GET.get('description')
    print(description)
    incidents = Incident.objects.filter(description__contains=description)
    list_response = []
    for incident in incidents:
        list_response.append(incident.to_json())
    return JsonResponse(list_response,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def search_incidents_from_to(request: HttpRequest) -> JsonResponse:
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')
    if from_date is not None and to_date is not None:
    
        incidents = Incident.objects.filter(open_incident_time__range=[from_date,to_date])
        list_response = []
        for incident in incidents:
            list_response.append(incident.to_json())
        return JsonResponse(list_response,safe=False)
    return JsonResponse({})

@csrf_exempt
@require_http_methods(["GET"])
def get_all_incidents(request: HttpRequest) -> JsonResponse:
    incidents = Incident.objects.all()
    list_response = []
    for incident in incidents:
        list_response.append(incident.to_json())
    return JsonResponse(list_response,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def get_all_incidents_type(request: HttpRequest) -> JsonResponse:
    incident_types = IncidentType.objects.all()
    list_response = []
    for incident_type in incident_types:
        list_response.append(incident_type.to_json())
    return JsonResponse(list_response,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def get_all(request: HttpRequest) -> JsonResponse:
    incidents = Incident.objects.all()
    list_incidents = []
    for incident in incidents:
        list_incidents.append(incident.to_json())
    incident_types = IncidentType.objects.all()
    list_incident_types = []
    for incident_type in incident_types:
        list_incident_types.append(incident_type.to_json())
    response = {
        "incidents": list_incidents,
        "incident_types": list_incident_types
    }
    print(response)
    return JsonResponse(response)

@csrf_exempt
@require_http_methods(["POST"])
def create_incident(request: HttpRequest) -> JsonResponse:
    try:
        body = __get_request_body__(request)
        incident_type_id = body.get('incident_type_id')
        description = body.get('description')
        create_time = body.get('create_time')
        open_incident_time = body.get('open_incident_time')
        close_incident_time = body.get('close_incident_time')
        acknowledge_time = body.get('acknowledge_time')
        incident_type = None
        if incident_type_id is not None:
            incident_type = IncidentType.objects.get(incident_type_id)
        obj = Incident.objects.create(
            description=description,
            create_time=create_time,
            open_incident_time=open_incident_time,
            close_incident_time=close_incident_time,
            acknowledge_time=acknowledge_time,
            incident_type=incident_type
        )
        obj.save()
    except Exception as err:
        return JsonResponse({"message": f"{err.__repr__()}"}, status=500)
    return JsonResponse(obj.to_json())

@csrf_exempt
@require_http_methods(["POST"])
def create_type_incident(request: HttpRequest) -> JsonResponse:
    try:
        body = __get_request_body__(request)
        name = body.get('name')
        style = body.get('style')
        if name is None:
            return JsonResponse({"message": "field \"name\" can't be null!"})
        type_incident = IncidentType.objects.create(name=name,style=style)
        type_incident.save()
    except Exception as err:
        return JsonResponse({"message": f"{err.__repr__()}"}, status=500)
    return JsonResponse(type_incident.to_json())

def __get_request_body__(request: HttpRequest) -> dict:
    body_unicode = request.body.decode('utf-8')
    return json.loads(body_unicode)