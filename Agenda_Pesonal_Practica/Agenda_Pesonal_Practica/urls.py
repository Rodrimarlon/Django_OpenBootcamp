from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contacts.urls')),
    path('to_do', include('to_do.urls')),
]
