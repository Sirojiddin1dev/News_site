from django.shortcuts import render, redirect
from .models import Ad


def create_ad_view(request):
    if request.method == 'POST':
        user = request.POST['user']
        name = request.POST['name']
        img = request.FILES.get('img')
        price = request.POST['price']
        address = request.POST['address']
        date = request.POST['date']
        description = request.POST['description']
        category = request.POST['category']
        view = request.POST['view']
        Ad.objects.create(
            user_id=user,
            name=name,
            img=img,
            price=price,
            address=address,
            date=date,
            description=description,
            category=category,
            view=view,
        )
        return redirect('index_url')


def edit_ad_view(request, pk):
    ad = Ad.objects.get(pk=pk)
    if request.method == "POST":
        user = request.POST.get('user')
        name = request.POST.get('name')
        img = request.POST.get('img')
        price = request.POST.get('price')
        address = request.POST.get('address')
        date = request.POST.get('date')
        description = request.POST.get('description')
        category = request.POST.get('category')
        view = request.POST.get('view')
        ad.username = ad
        if img is not None:
            ad.img = img
        ad.save()
        context = {
            'ad': ad
        }
        return render(request, 'index.html', context)
    context = {
        'ad': ad
    }
    return render(request, 'index.html', context)


def delete_ad_view(request, pk):
    ad = Ad.objects.get(pk=pk)
    ad.delete()
    return redirect("index_url")