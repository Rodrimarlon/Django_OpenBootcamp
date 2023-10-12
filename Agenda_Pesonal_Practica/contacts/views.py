from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):

    contacts = Contact.objects.filter(name__contains=request.GET.get('search', ''))
    
    context = {
        'contacts': contacts
    }
    return render(request, 'contact/index.html', context)