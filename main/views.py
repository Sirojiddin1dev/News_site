from django.shortcuts import render, redirect
from dashboard.models import Ad

def index_view(request):
    context = {
        'ad': Ad.objects.all().order_by('-id')[:8]
    }
    return render(request, 'index.html', context)


def single_ad_view(requet, pk):
    single_ad = Ad.objects.get(pk=pk)
    context = {
        'single_ad': single_ad
    }
    return render(request, 'poster-page.html', context)