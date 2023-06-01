from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
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
    if request.method =='POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmers')
    context = {'form':form}

    return render (request,'farmer_form.html',context)


