from django.shortcuts import render
from django.http import HttpResponse
from . import models

def comments(request):
    return HttpResponse('Hola Mundo')

def create(request):
    # comment = models.Comment(name='Marlon', score=5, comment='Esto es un comentario de prueba')
    # comment.save()
    comment = models.Comment.objects.create(name='Melani', score='2', comment='Esto es otro comentario', signature='que lo que')
    return HttpResponse('Hola Mundo, desde create')


def delete(request):
    # comment = models.Comment.objects.get(id=1)
    # comment.delete()
    models.Comment.objects.filter(id=2).delete()
    return HttpResponse('Rura para borrar comentarios')