from django.urls import path
from .views import *
from dashboard.views import create_ad_view

urlpatterns = [
    path('index/', index_view, name='index_url'),
    path('create/', create_ad_view, name='create_ad_url'),
    path('single_ad/<int:pk>/', single_ad_view, name='single_ad_url')
]
