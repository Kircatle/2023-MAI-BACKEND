from django.shortcuts import render

import json

from django.core.handlers.asgi import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import IncidentType, Incident


@csrf_exempt
@require_http_methods(["GET"])
def search_by_incident_type(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"1":1})

@csrf_exempt
@require_http_methods(["GET"])
def search_incidents_from_to(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"1":1})


@csrf_exempt
@require_http_methods(["GET"])
def get_all_incidents(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"1":1})

@csrf_exempt
@require_http_methods(["GET"])
def get_all_incidents_type(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"1":1})

@csrf_exempt
@require_http_methods(["POST"])
def create_incident(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"1":1})


@csrf_exempt
@require_http_methods(["POST"])
def create_type(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"1":1})
