from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(max_length=10)
    emailid = models.EmailField(max_length=60)
    age = models.IntegerField(max_length=5)
    gender = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField(default=0.00, max_length=10)
    unit = models.IntegerField(default=0, max_length=10)
    date = models.DateField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField(default=0.00, max_length=10)
    duration = models.IntegerField(default=0, max_length=10)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    emailid = models.EmailField(max_length=60)
    age = models.IntegerField(max_length=5)
    gender = models.CharField(max_length=40)
    plan = models.CharField(max_length=40)
    joindate = models.DateField()
    expiredate = models.DateField
    initialamount = models.FloatField(default=0.00 ,max_length=10)

    def __str__(self):
        return self.name