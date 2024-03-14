from django.urls import path
from views import *

urlpatterns = [
    path('index_view', index_view),
    path('search_news_view', search_news_view),
    path('create_email_view', create_email_view),
    path('singe_news_view', singe_news_view),
    path('filter_by_category_view', filter_by_category_view),
    path('filter_news_by_tag_view', filter_news_by_tag_view),
]
