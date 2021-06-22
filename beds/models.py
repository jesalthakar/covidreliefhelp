from django.db import models

# Create your models here.
class Bed(models.Model):
    name =  models.CharField(default=" ",max_length=50)
    city = models.CharField(max_length=200)
    Address = models.TextField(blank = True, default = "No location")
    hospital = models.CharField(blank = True, max_length=200)
    poc = models.CharField(max_length=200)
    additional_info = models.TextField(blank= True, default= " ")
    created = models.DateTimeField()
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name}-{self.city}-{self.created.strftime('%d/%m/%Y')}"
