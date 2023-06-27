from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from farmersapp.forms import FarmForm, FarmerForm, VentureForm
from farmersapp.models import Farmer, Venture, Farm
from users.forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
#from farmersapp.forms import FarmerForm


# Create your views here.
def register(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'User account created')
            login(request,user)
            return redirect('ventures')
        else:
            messages.error(request,'error occurred')
    context = {'page':page,'form':form}
    return render (request,'register.html',context)

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('ventures')

def login_user(request, template_name='login.html'):
    """Login view."""
    form = AuthenticationForm(request)
    if form.is_valid():
        # Authenticate the user.
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user is not None:
            # Login the user.
            login(request, user)
            return redirect(request.GET.get('next', '/'))

    return render(request, template_name, {'form': form})


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
            farmer = form.save(commit= False)
            form.save()
            return redirect('createfarm',farmer.id)
    context = {'form':form}

    return render (request,'farmer_form.html',context)

def createFarm(request,pk):
    form = FarmForm
    farmer = Farmer.objects.get(id = pk)
    if request.method =='POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.farmer = farmer
            form.save()
            return redirect('createventure',farm.id)
            
    context = {'form':form}

    return render (request,'farm_form.html',context)

def createVenture(request,pk):
    form = VentureForm
    farm = Farm.objects.get(id = pk)
    if request.method =='POST':
        form = VentureForm(request.POST)
        if form.is_valid():
            venture = form.save(commit=False)
            venture.farm = farm
            form.save()
            return redirect('ventures')
    context = {'form':form}

    return render (request,'venture_form.html',context)

def updateFarmer(request,pk):
    farmer = Farmer.objects.get(id = pk)
    form = FarmerForm(instance=farmer)
    if request.method =='POST':
        form = FarmerForm(request.POST,instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('ventures')
    context = {'form':form}

    return render (request,'farmer_form.html',context)

def ventures(request):
    mventures = Venture.objects.all()
    context = {'mventures': mventures}
    return render(request,'ventures.html',context)

def details(request,pk):
    mdetails = Venture.objects.get(id = pk)
    context = {'mdetails': mdetails}
    return render(request,'details.html',context)

def farms(request):
    mfarms = Farm.objects.all()
    context = {'mfarms': mfarms}
    return render(request,'farms.html',context)

def deleteObject(request,pk):
    farmer = Farmer.objects.get(id = pk)
    if request.method == 'POST':
        farmer.delete()
        return redirect('farmers')
    context = {'mfarmer':farmer}
    return render(request,'delete.html',context)


