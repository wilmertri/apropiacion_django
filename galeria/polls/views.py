# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Imagen


# Create your views here.
@csrf_exempt
def index(request):
    if request.user.is_authenticated():
        lista_imagenes = Imagen.objects.filter(user=request.user)
    else:
        lista_imagenes = Imagen.objects.all()

    context = {'lista_imagenes': lista_imagenes}

    # return render(request, 'polls/index.html', context)
    return HttpResponse(serializers.serialize("json", lista_imagenes))

@csrf_exempt
def add_image(request):
    if request.method == 'POST':
        new_imagen = Imagen(url=request.POST['url'],
                            title=request.POST['title'],
                            description=request.POST.get('description'),
                            type=request.POST.get('type'),
                            imageFile=request.FILES['imageFile'],
                            user=request.user);

        new_imagen.save();  # Guardar datos en la DB

    # return render(request, 'polls/image_form.html', {'form':form})
    return HttpResponse(serializers.serialize('json', [new_imagen]))


@csrf_exempt
def add_user_view(request):
    print 'Entro'
    if request.method == 'POST':
        jsonUser = json.loads(request.body)

        username = jsonUser['username']
        first_name = jsonUser['first_name']
        last_name = jsonUser['last_name']
        password = jsonUser['password']
        email = jsonUser['email']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
        print 'Usuario Guardado'
    return HttpResponse(serializers.serialize("json", [user_model]))


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            mensaje = 'Ok'
        else:
            mensaje = 'Nombre de usuario o clave invalido'
        print mensaje
    return JsonResponse({'mensaje': mensaje})


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'mensaje': 'Ok'})
    # return HttpResponseRedirect(reverse('images:index'))


@csrf_exempt
def isLogged_view(request):
    if request.user.is_authenticated():
        mensaje = 'Ok'
    else:
        mensaje = 'No'

    return JsonResponse({'mensaje': mensaje})


@csrf_exempt
def ver_imagenes(request):
    return render(request, "polls/index.html")


@csrf_exempt
def agregar_imagen(request):
    return render(request, "polls/image_form.html")


@csrf_exempt
def agregar_usuario(request):
    return render(request, "polls/registro.html")


@csrf_exempt
def ingresar(request):
    return render(request, "polls/login.html")
