from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from farmersapp.forms import FarmForm, FarmerForm, VentureForm
from farmersapp.models import Farmer, Venture, Farm
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

def updateFarmer(request,pk):
    farmer = Farmer.objects.get(id = pk)
    form = FarmerForm(instance=farmer)
    if request.method =='POST':
        form = FarmerForm(request.POST,instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('farmers')
    context = {'form':form}

    return render (request,'updatefarmer_form.html',context)

def createFarm(request):
    form = FarmForm
    if request.method =='POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farms')
    context = {'form':form}

    return render (request,'farm_form.html',context)

def createVenture(request):
    form = VentureForm
    if request.method =='POST':
        form = VentureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventures')
    context = {'form':form}

    return render (request,'venture_form.html',context)

def ventures(request):
    mventures = Venture.objects.all()
    context = {'mventures': mventures}
    return render(request,'ventures.html',context)

def farms(request):
    mfarms = Farm.objects.all()
    context = {'mfarms': mfarms}
    return render(request,'farms.html',context)


