from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index_url'),
    path('contact/', views.contact, name = 'index_url'),
]