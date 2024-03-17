from django.shortcuts import render
from dashboard.models import Ad
from account.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index_view(request):
    context = {
        'ad': Ad.objects.all().order_by('-id')[:8]
    }
    return render(request, 'index.html', context)


def single_ad_view(request, pk):
    single_ad = Ad.objects.get(pk=pk)
    user = single_ad.user
    count = Ad.objects.filter(user=user).order_by('id').count
    single_ad.view += 1
    single_ad.save()
    context = {
        'single_ad': single_ad,
        'user': user,
        'count': count
    }
    return render(request, 'poster-page.html', context)


def user_detail_view(request, pk):
    user = User.objects.get(pk=pk)
    count = Ad.objects.filter(user=user).order_by('id').count
    ad = Ad.objects.filter(user=user).order_by('-id')[:8]
    context = {
        'user': user,
        'count': count,
        'ad': ad,
    }
    return render(request, 'profile.html', context)


def ad_filters_view(request):
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    region = request.GET.get('region')

    ad = Ad.objects.all()

    if category:
        ad = ad.filter(category=category)
    if min_price:
        ad = ad.filter(price__gte=min_price)
    if max_price:
        ad = ad.filter(price__lte=max_price)
    if region:
        ad = ad.filter(address=region)

    context = {
        'a': ad
    }
    return render(request, 'posters.html', context)


def search_view(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Ad.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'query': query, 'results': results})


def kochmas_mulk_view(request):
    category = Ad.objects.filter(category="Ko'chmas mulk")
    context = {
        'a': PegenatorPage(category, 5, request)
    }
    return render(request, 'mulk.html', context)


def ish_orni_view(request):
    category = Ad.objects.filter(category="Ish o'rni")
    context = {
        'a': PegenatorPage(category, 5, request)
    }
    return render(request, 'ish.html', context)


def texnika_view(request):
    category = Ad.objects.filter(category="Elektrotexnika")
    context = {
        'a': PegenatorPage(category, 5, request)
    }
    return render(request, 'texnika.html', context)


def transport_view(request):
    category = Ad.objects.filter(category="Transport")
    context = {
        'a': PegenatorPage(category, 5, request)
    }
    return render(request, 'mulk.html', context)


def PegenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list
