from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm


def form(request):
    comment_form = CommentForm
    return render(request, 'form.html', {'comment_form': comment_form})