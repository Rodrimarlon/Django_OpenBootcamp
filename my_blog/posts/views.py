from django.shortcuts import render
from .models import Author, Entry


def queries(request):
    #Obtener todos los elementos
    authors = Author.objects.all() 

    # Obtener datos filtrados por condición
    filtered = Author.objects.filter(email='wlove@example.net')

    # Obtener un unico objeto (filtrado)
    author = Author.objects.get(id=10)

    # Obtener solo 10 elementos
    limits = Author.objects.all()[40::-1]

    return render(request, 'post/queries.html', 
                  {'authors': authors, 'filtered': filtered,
                   'author': author, 'limits': limits})