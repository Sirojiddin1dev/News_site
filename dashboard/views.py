from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from . import models
from django.contrib.auth.decorators import login_required


@permission_classes([IsAuthenticated])
def index(request):
    context = {
        'user': request.user,
        'comments': models.Comment.objects.all()
    }
    return render(request,'index.html',context)


@permission_classes([IsAuthenticated])
def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        created = models.Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            message=message,
        )
    return render(request, 'contact.html', context)