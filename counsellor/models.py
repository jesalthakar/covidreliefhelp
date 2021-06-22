from django.db import models



# Create your models here.
class Counsellor(models.Model):
    Name = models.CharField(default = "" ,max_length=50)
    Counsellor_Name = models.CharField(max_length=12)
    Contact_nos = models.CharField(default = "" ,max_length=50)
    Location = models.CharField(blank=True,max_length=200)
    additional_info = models.TextField(blank = True)
    created = models.DateTimeField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Name}-{self.Counsellor_Name}-{self.created}"
