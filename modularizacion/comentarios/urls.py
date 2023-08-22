from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments, name='comments'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
]