from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from farmersapp.forms import FarmForm, FarmerForm, VentureForm
from farmersapp.models import Farmer, Venture, Farm
from users.forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
            return redirect('createfarmer')
        else:
            messages.error(request,'error occurred')
    context = {'page':page,'form':form}
    return render (request,'register.html',context)
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('ventures')

def login_user(request, template_name='login.html'):
    """Login view."""
    if request.method == 'POST':
        _username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = _username)
        except Exception as e:
            print('Username does not exist',e)
        print(password)
        user = authenticate(username=_username,
                            password=password)
        if user is not None:
            # Login the user.
            login(request, user)
            if (request.GET.get('next', '/')):
                return redirect(request.GET.get('next', '/'))
            else:
                return redirect('ventures')
    return render(request, template_name)

@login_required
def farmers(request):
    mfarmers = Farmer.objects.all()
    context = {'mfarmers': mfarmers}
    return render(request,'farmers.html',context)
@login_required
def farmer(request,pk):
   return render(request,'signle-farmer.html')
@login_required
def createFarmer(request):
    form = FarmerForm
    user = request.user
    farmer = Farmer.objects.get(user = user)
    print(farmer)
    if (farmer.surname is not None): # we have a farmer with all details
        farm = Farm.objects.get(farmer = farmer)#let's get farmer's farm
        if (farm is not None):
            return redirect('createventure',farm.id) #create venture
        else:
            return redirect ('createfarm',farmer.id)
    #go ahead and create farmer        
    if request.method =='POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createfarm',farmer.id)
            
    context = {'form':form}
    return render (request,'farmer_form.html',context)
@login_required
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
@login_required
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
@login_required
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
def venturesProv(request,pk):
    if pk =='PVT':
        cct = Q(farm__tenure_type = 'CCT' )#consolidated title
        title = Q(farm__tenure_type = 'Ttl' )#Title Deed
        dg = Q(farm__tenure_type = 'DG' )#Deed of grant
        ventures = Venture.objects.filter(cct|title|dg)
    else:
        ventures = Venture.objects.filter(farm__province=pk)
    print(ventures)
    context = {'mventures': ventures}
    return render(request,'ventures.html',context)
@login_required    
def dashboard(request,user):
    dash_stuff = Venture.objects.get(farm.farmer.user == user)
    context = {'mdetails': dash_stuff}
    return render(request,'details.html',context)

def ventures(request):
    search_query = request.GET.get('Search_Query')
    print(search_query)
    filtered_data =''
    if search_query is not None:
        thequery = Q(farm__farm_name__icontains = search_query) | Q(farm__district__icontains = search_query) | Q(farm__farmer__name__icontains = search_query)
        filtered_data = Venture.objects.filter(farm__farm_name__icontains = search_query)
    else:
        filtered_data = Venture.objects.all()
    #mventures = Venture.objects.filter(filtered_data)
    context = {'mventures': filtered_data}
    return render(request,'ventures.html',context)

def details(request,pk):
    mdetails = Venture.objects.get(id = pk)
    context = {'mdetails': mdetails}
    return render(request,'details.html',context)

@login_required
def farms(request):
    mfarms = Farm.objects.all()
    context = {'mfarms': mfarms}
    return render(request,'farms.html',context)
@login_required
def deleteObject(request,pk):
    farmer = Farmer.objects.get(id = pk)
    if request.method == 'POST':
        farmer.delete()
        return redirect('farmers')
    context = {'mfarmer':farmer}
    return render(request,'delete.html',context)


