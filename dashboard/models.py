from django.db import models
from account.models import User
from django.core.validators import RegexValidator


class Comment(models.Model):
    text = models.TextField()


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            message='Invalide email',
            code='Invalid email'
        )
    ])
    phone_number = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    bio = models.CharField(max_length=255, null=True, blank=True)
