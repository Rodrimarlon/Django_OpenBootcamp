from django.shortcuts import render

def simple(request):
    return render(request, 'simple.html')

def posts(request):
    return render(request, 'posts/post.html', {})

def dinamico(request, name):
    categories = ['code', 'disign', 'marketing', 'finance']
    context = {'name': name, 'categories': categories}
    return render(request, 'dinamico.html', context)