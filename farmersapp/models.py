from django.db import models
import uuid

# Create your models here.
tenure = (
   ('Off','Offer Letter'),
   ('99','99-Year Lease'),
   ('A1','A1 Permit'),
   ('AP', 'A1 Temporal Permit'),
   ('A2','A2 Permit'),
   ('Ttl','Title Deed'),
   ('DG','Deed of Grant'),
   ('CCT','Certificate of Consolidated Title'),
)
gender = (
   ('M','Male'),
   ('F','Female'),
)
water = (
   ('D','Dam'),
   ('R','River'),
   ('B','Borehole'),
   ('W', 'Weir'),
   ('Wl','Well'),
   ('N','None'),
)
class Farmer(models.Model):
    name = models.CharField(max_length=250)
    othername = models.CharField(max_length=250,null=True, blank=True)
    surname = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    gender = models.CharField(max_length=10,choices=gender)
    national_id = models.CharField(max_length=30,null =True,unique=True)
    id = models.UUIDField(default=uuid.uuid1,unique=True,primary_key=True,editable=False)

    def __str__(self):
     return self.name +" "+ self.surname

province = (
   ('MTN','Matabeleland North'),
   ('MTS','Matabeleland South'),
   ('MSE','Mashonaland East'),
   ('MSW','Mashonaland West'),
   ('MSC','Mashonaland Central'),
   ('MAN','Manicaland'),
    ('MSV','Masvingo'),
    ('MID','Midlands'),
    ('HRE','Harare'),
    ('BYO','Bulawayo'),
)
class Farm(models.Model):
    farmer = models.ForeignKey(Farmer,on_delete = models.CASCADE)
    farm_name = models.CharField(max_length=500)
    plot_number = models.CharField(max_length=250,null=True, blank=True)
    extend = models.DecimalField(max_digits= 10,decimal_places= 4)
    district = models.CharField(max_length=20)
    province = models.CharField(max_length=250,choices=province)
    ward = models.CharField(max_length=10,null=True, blank=True)
    tenure_type = models.CharField(max_length=50,choices=tenure)
    irrigation =models.CharField(max_length=250,null= True,default ="Do you have irrigation",choices=(('Y','Yes'),('N','No')))
    water_availability  = models.CharField(max_length=250,choices=water)
    id = models.UUIDField(default=uuid.uuid1,unique=True,primary_key=True,editable=False)

    def __str__(self):
     return self.farm_name

class Venture(models.Model):
   farm = models.ForeignKey(Farm,on_delete = models.CASCADE)
   descripiton = models.TextField()
   supporting_images = models.CharField(max_length=250,null = True, blank=True)
   amount = models.DecimalField(max_digits= 20,decimal_places= 2,null = True,blank = True)
   id = models.UUIDField(default=uuid.uuid1,unique=True,primary_key=True,editable=False)

