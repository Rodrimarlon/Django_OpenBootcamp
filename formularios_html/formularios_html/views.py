from django.shortcuts import render 
from django.http import HttpResponse


def getform(request):
    return render(request, 'form.html', {})


def getgoal(request):
    if request.method != 'GET':
        return HttpResponse('El metodo POST no esta soportado para esta ruta')
    
    name = request.GET['name']
    last_name = request.GET['last_name']
    return render(request, 'success.html', {'name':name, 'last_name':last_name})


def postform(request):
    return HttpResponse('hola')


def postgoal(request):
    return HttpResponse('en construccion')