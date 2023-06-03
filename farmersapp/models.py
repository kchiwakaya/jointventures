from django.db import models
import uuid

# Create your models here.
class Farmer(models.Model):
    name = models.CharField(max_length=250)
    othername = models.CharField(max_length=250,null=True, blank=True)
    surname = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    id = models.UUIDField(default=uuid.uuid1,unique=True,primary_key=True,editable=False)

    def __str__(self):
     return self.name +" "+ self.surname


class Farm(models.Model):
    farmer = models.ForeignKey(Farmer,on_delete = models.CASCADE)
    farm_name = models.CharField(max_length=500)
    plot_number = models.CharField(max_length=250,null=True, blank=True)
    extend = models.DecimalField(max_digits= 10,decimal_places= 4)
    district = models.CharField(max_length=20)
    province = models.CharField(max_length=250)
    ward = models.CharField(max_length=10,null=True, blank=True)
    tenure_type = models.CharField(max_length=50)
    water_availability  = models.CharField(max_length=250)
    id = models.UUIDField(default=uuid.uuid1,unique=True,primary_key=True,editable=False)

    def __str__(self):
     return self.farm_name

class Venture(models.Model):
   farm = models.ForeignKey(Farm,on_delete = models.CASCADE)
   descripiton = models.TextField()
   supporting_images = models.CharField(max_length=250,null = True, blank=True)
   amount = models.DecimalField(max_digits= 20,decimal_places= 2,null = True,blank = True)
   id = models.UUIDField(default=uuid.uuid1,unique=True,primary_key=True,editable=False)

