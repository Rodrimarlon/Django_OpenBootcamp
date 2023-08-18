from django.http import HttpResponse

def saludo(request):
    return HttpResponse("<h1>Hola Mundo...</h1> ")

def despedida(request):
    return HttpResponse("<h1>Hasta Luego</h1>")

def practica(request):
    return HttpResponse("<h1>Esto es otra respuesta atravez de una url</h1>")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("En hora buena ya eres adulto")
    else:
        return HttpResponse("Esperemos un poco no puedes tomar aun jajaja")
