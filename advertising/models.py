from django.db import models

class Advertising(models.Model):
    img = models.ImageField(upload_to='advertising_photo')
    end_time = models.DateTimeField()
    STATUS_CHOICES = (
        ('public','public'),
        ('drop','drop'),

    )
    status = models.CharField(max_lenght=200, choices=STATUS_CHOICES,default=public)



