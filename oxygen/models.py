from django.db import models
from django.utils import timezone




# Create your models here.



class Oxygen(models.Model):
    name =  models.CharField(default="",max_length=50)
    city = models.CharField(max_length=200)
    Address = models.TextField(blank=True, default = "No location")
    hospital = models.CharField(blank= True, max_length=200)
    poc = models.CharField(max_length=200)
    additional_info = models.TextField(blank= True, default= " ")
    created = models.DateTimeField(default=timezone.now())
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name}-{self.city}-{self.Address}-{self.hospital}-{self.poc}-{self.additional_info}-{self.created.strftime('%d/%m/%Y')}"
