from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_url")
def index(request):
    context = {
        'user': request.user,
        'comments': models.Comment.objects.all()
    }
    return render(request,context)


@login_required(login_url="login_url")
def contact(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        bio = request.POST['bio']
        created = models.Contact.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone_number = phone_number,
            bio = bio,
        )