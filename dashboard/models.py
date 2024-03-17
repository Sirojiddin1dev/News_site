from django.db import models
from account.models import *


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    img = models.ImageField(upload_to='ad_img/')
    price = models.DecimalField(decimal_places=2, max_digits=12)
    address = models.CharField(max_length=55)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    Category = (
        ("Ko'chmas mulk", "Ko'chmas mulk"),
        ('Transport', 'Transport'),
        ('Elektrotexnika', 'Elektrotexnika'),
        ("Ish o'rni", "Ish o'rni"),
    )
    category = models.CharField(max_length=100, choices=Category)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.name
