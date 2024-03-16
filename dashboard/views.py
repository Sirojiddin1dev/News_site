from django.shortcuts import render, redirect
from .models import Ad


def create_ad_view(request):
    if request.method == 'POST':
        user = request.POST['user']
        name = request.POST['name']
        img = request.FILES.get('img')
        price = request.POST['price']
        address = request.POST['address']
        description = request.POST['description']
        category = request.POST['category']
        Ad.objects.create(
            user_id=request.user,
            name=name,
            img=img,
            price=price,
            address=address,
            description=description,
            category=category,
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
        ad.user = user
        ad.name = name
        ad.img = img
        ad.price = price
        ad.address = address
        ad.date = date
        ad.description = description
        ad.category = category
        ad.view = view
        if img is not None:
            ad.img = img
        ad.save()
        return redirect("index_url")
    context = {
        'ad': ad
    }
    return render(request, 'index.html', context)


def delete_ad_view(request, pk):
    ad = Ad.objects.get(pk=pk)
    ad.delete()
    return redirect("index_url")