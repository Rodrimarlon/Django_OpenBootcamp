from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse


def queries(request):
    #Obtener todos los elementos
    authors = Author.objects.all() 

    # Obtener datos filtrados por condición
    #filtered = Author.objects.filter(email='wlove@example.net')

    # Obtener un unico objeto (filtrado)
    author = Author.objects.get(id=10)

    # Obtener solo 10 elementos
    limits = Author.objects.all()[40::-1]

    # Obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')

    # Obtener todos los elementos cuyo id sea menor o igual a 15
    """ Los para metros para pasarcelos a filter y realizar estas consultas son:
        __lte : menor o igual que (lower than equals)
        __gte : mayor o igual que (greater than equals)
        __lt : menor que (lower than)
        __gt : mayor que (greater than)
        __contains : contiene
        __exact : exacto
    """
    # filtered = Author.objects.filter(id__lte=15)

    #Obtener todos los autores que contienen en su nombre la palabra yes
    filtered = Author.objects.filter(name__contains="the")




    return render(request, 'post/queries.html', 
                  {'authors': authors, 'filtered': filtered,
                   'author': author, 'limits': limits,
                   'orders': orders})


def update(request):
    author = Author.objects.get(id=1)
    author.name = 'Marlon'
    author.email = 'marlon@example.com'
    author.save()

    return HttpResponse('Datos Actualizados')