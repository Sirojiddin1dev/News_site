from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *


def index_view(request):
    context = {
        'banner_news': News.objects.all().order_by('-id')[:3],
        'categories': Category.objects.all(),
        'popular_news':News.objects.all().order_by('-view')[:3],
        'tags': Tag.objects.all(),
        'news_2':News.objects.all().order_by('-id')[3:6]
    }
    return render(request, "index.html", context)


def search_news_view(request):
    title = request.GET.get('title')
    context = {
        'news': News.objects.filter(title__icontains=title),
        'categories': Category.objects.all()
    }
    return render(request, 'search_news.html', context)


def create_email_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        Newsletter.objects.create(
            email=email,
        )
    return redirect('index_url')


def singe_news_view(request, pk):
    new = News.objects.get(pk=pk)
    new.view +=1
    new.save()
    context = {
        'new': new,
        'categories': Category.objects.all()
    }
    return render(request, 'single.html', context)


def filter_by_category_view(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'news_by_category':News.objects.filter(category=category),
        'categories': Category.objects.all()
    }
    return render(request,'category-detail.html',context)


def filter_news_by_tag_view(request, pk):
    tag = Tag.objects.get(pk=pk)
    context = {
        'news_by_tag': News.objects.filter(tag__name=tag)
    }
    return render(request, 'news-by-tag.html', context)



