from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm, ContactForm


def form(request):
    comment_form = CommentForm({'name': 'juanjo', 'url': 'https://open-bootcamp.com', 'comment': 'comentario'})
    return render(request, 'form.html', {'comment_form': comment_form})

def goal(request):
    if request.method != 'POST':
        return HttpResponse('Metodo Incorrecto')
    
    return HttpResponse(request.POST['name'])


def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Todas las acciones que quicieramos hacer con los datos del formulario
            return HttpResponse('post')
        else:
            # Comunicamos al usuario que los datos son errores
            return render(request, 'widget.html', {'form': form})