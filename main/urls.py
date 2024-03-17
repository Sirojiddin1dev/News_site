from django.urls import path
from .views import *
from dashboard.views import create_ad_view

urlpatterns = [
    path('index/', index_view, name='index_url'),
    path('create/', create_ad_view, name='create_ad_url'),
    path('single_ad/<int:pk>/', single_ad_view, name='single_ad_url'),
    path('user-detail/<int:pk>/', user_detail_view, name='user_detail_url'),
    path('ad-filter/', ad_filters_view, name='ad_filter_url'),
    path('search/', search_view, name='search'),
    path('kochmas-mulk/', kochmas_mulk_view, name='mulk'),
    path('ish-orni/', ish_orni_view, name='ish'),
    path('texnika/', texnika_view, name='texnika'),
    path('transport/', transport_view, name='transport'),
]
