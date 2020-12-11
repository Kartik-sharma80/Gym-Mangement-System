from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(max_length=10)
    emailid = models.EmailField(max_length=60)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=40)

    def __str__(self):
        return self.name

