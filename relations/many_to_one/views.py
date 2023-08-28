from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date


def create(request):
    rep = Reporter(first_name='Marlon', last_name='Rodriguez', email='marlon@example.com')
    rep.save()

    art1 = Article(headline='Articulo 1', date=date(2022,5,5), reporter=rep)
    art1.save()

    art2 = Article(headline='Articulo 2', date=date(2023,4,8), reporter=rep)
    art2.save()

    art3 = Article(headline='Articulo 3', date=date(2020,5,7), reporter=rep)
    art3.save()

    # Consultando el email del reportero que creo el articulo 1
    #result = art1.reporter.email

    # Atrabes de _set vamos a acceder a los elmentos, y de hay hacer
    # nuestras Consultas
    result = rep.article_set.all()


    return HttpResponse(result)