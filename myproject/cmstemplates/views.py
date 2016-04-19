from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse
from django.template.loader import get_template
from django.template import Context
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.


def index(request, peticion_id):

    try:
        solicitud = Pages.objects.get(id=int(peticion_id))
        #en vez del id lo podemos hacer tambien con el nombre pero esta mejor asi
    except Pages.DoesNotExist:
        return HttpResponse('Page Not Found')
    respuesta = 'Hola, soy ' + solicitud.name + ": " + str(solicitud.page)
    return HttpResponse(respuesta)


@csrf_exempt
def nuevo_recurso(request):

    if request.method == "GET":
        template = get_template('formulario.html')
        Context = ({})
        Respuesta = template.render(Context)
    elif request.method == "POST":  #cuando haga el put con poster acordarme de poner la barra al final que me ha dado ya error 4 veces
        nombre = request.POST['nombre']
        try:
            pagina = request.POST['pagina']
        except MultiValueDictKeyError:
            pagina = False
        contenido = Pages(name =str(nombre), page= str(pagina))
        contenido.save()
        Respuesta = "Pagina creada correctamente"
    return HttpResponse(Respuesta)


def paginanueva(request, nombre, pagina):
    if request.method == "GET":
        p = Pages(name=nombre, page=pagina)
        p.save()
    elif request.method == "PUT":  #cuando haga el put con poster acordarme de poner la barra al final que me ha dado ya error 4 veces
        if request.user.is_authenticated():
            info = request.body
            p = Pages(name=nombre, page=info)
            p.save()
            respuesta = 'Todo ha ido bien'
        else:
            respuesta = 'El usuario no esta autenticado'
    return HttpResponse(respuesta)

def muestra_paginas(request):
    if request.user.is_authenticated():
        respuesta1 = 'Logged in as ' + request.user.username + ' .' + '<a href="/logout">Logout</a>'
    else:
        respuesta1 = 'Not logged in.' + ' <a href="/login">Login</a>'

    lista_paginas = Pages.objects.all()
    respuesta2 = "<ol>"
    for pag in lista_paginas:
        respuesta2 += '<li><a href="/' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta2 += "</ol>"
    template = get_template('plantilla.html')
    Context = ({'login': respuesta1, 'contenido': respuesta2})
    Rellenar = template.render(Context)
    return HttpResponse(Rellenar)


def usuario(request):
    respuesta = "Eres " + request.user.username
    return HttpResponse(respuesta)
