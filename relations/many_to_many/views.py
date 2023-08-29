from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

def create(request):
    """art1 = Article(headline='Articulo Primero')
    art1.save()

    art2 = Article(headline='Articulo Segundo')
    art2.save()

    art3 = Article(headline='Articulo Tercero')
    art3.save()

    pub1 = Publication(title='Publicacion Uno')
    pub1.save()
    pub2 = Publication(title='Publicacion Dos')
    pub2.save()
    pub3 = Publication(title='Publicacion Tres')
    pub3.save()
    pub4 = Publication(title='Publicacion Cuatro')
    pub4.save()
    pub5 = Publication(title='Publicacion Cinco')
    pub5.save()
    pub6 = Publication(title='Publicacion Seis')
    pub6.save()"""

    # Agragando la Relacion de Articulos con publicaciones

    """art1.publications.add(pub1)
    art1.publications.add(pub2)
    art2.publications.add(pub3)
    art2.publications.add(pub4)
    art3.publications.add(pub5)
    art3.publications.add(pub6)"""
    
    # Obteniendo las publicaciones relacionadas con nuestro articulo 1
    #result = art1.publications.all()

    # Obteniendo los articulos relacionados con la publicacion

    pub1 = Publication.objects.get(id=1)
    result1 = pub1.article_set.all()

    # Eliminar una relacion
    # art1.publications.remove(pub1)
    return HttpResponse(result1) 