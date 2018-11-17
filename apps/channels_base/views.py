from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.safestring import mark_safe
import json
from .models import User
from django.contrib import messages
import bcrypt, datetime


# Create your views here.

# def lobby(request):
#     response = "Hello World"
#     return HttpResponse(response)

def index(request):
    request.session['id'] = '0'
    request.session['user'] = ''
    return render(request, '../templates/index.html', {})

def register(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            p_word = bcrypt.hashpw(request.POST['Password'].encode(), bcrypt.gensalt())
            user = User.objects.create(Username=request.POST['Username'], Password = p_word)
            user.save()
            request.session['id'] = user.id
            request.session['user'] = user.Username
        return redirect('/lobby')
    else:
        return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            user = User.objects.get(Username = request.POST['L_Username'])
            request.session['id'] = user.id
            request.session['user'] = user.Username
            # request.session['id'] = User.objects.get(Username = request.POST['L_Username']).id
            # request.session['user'] = User.objects.get(id = request.session['id'])
        return redirect('/lobby')
    else:
        return redirect('/')

def lobby(request):
    if not request.session['id'] == 0:
        request.session['room_name'] = ''
        return render(request, '../templates/lobby.html', {})
    else:
        return redirect('/')
        

def room(request, room_name):
    if not request.session['id'] == 0:
        request.session['room_name'] = room_name
        return render(request, '../templates/room.html', {'room_name_json': mark_safe(json.dumps(room_name))})
    else:
        return redirect('/')
    # request.session['room_name'] = room_name
    # return render(request, '../templates/room.html', {'room_name_json': mark_safe(json.dumps(room_name))})