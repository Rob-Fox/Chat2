from django.shortcuts import render, HttpResponse, redirect
from django.utils.safestring import mark_safe
import json

# Create your views here.

# def index(request):
#     response = "Hello World"
#     return HttpResponse(response)

def index(request):
    return render(request, '../templates/index.html', {})

def room(request, room_name):
    return render(request, '../templates/room.html', {'room_name_json': mark_safe(json.dumps(room_name))
    })