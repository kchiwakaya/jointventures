from django.shortcuts import render
from django.http import HttpResponse
from farmersapp.forms import FarmerForm
from farmersapp.models import Farmer
#from farmersapp.forms import FarmerForm


# Create your views here.
def farmers(request):
    mfarmers = Farmer.objects.all()
    context = {'mfarmers': mfarmers}
    return render(request,'farmers.html',context)

def farmer(request,pk):
   return render(request,'signle-farmer.html')

def createFarmer(request):
    form = FarmerForm
    context = {'form':form}
    return render (request,'farmer_form.html',context)


