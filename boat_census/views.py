from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Owner,District,BoatType,Vessel,LandingSite,BoatClass,BoatUse,FuelType
from .forms import OwnerForm,DistrictForm,BoatTypeForm,VesselForm,LandingSiteForm,BoatClassForm,BoatUseForm,PropulsionForm,ColorForm,FuelTypeForm
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    #Home Page
    return render(request,'boat_census/index.html')

def owners_view(request):
    #For viewing the owners
    owners = Owner.objects.all()
    context = {'owners':owners}
    return render(request,'boat_census/owners.html',context)

def add_owner(request):
    #Enable users to add owners
    if request.method != 'POST':
        #Data has not been entered, present a new from
        form = OwnerForm()
    else:
        #Data has been submitted
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('boat_census:owners'))
    context = {'form':form}
    return render(request,'boat_census/add_owner.html',context)

def districts(request):
    #Show districts in the Database
    districts = District.objects.all()
    context = {'districts':districts}
    return render(request,'boat_census/districts.html',context)

def add_district(request):
    #Enable Users to add districts
    if request.method != 'POST':
        #Form has not been submitted, present a new form
        form = DistrictForm()
    else:
        #Form has been submitted, process data
        form = DistrictForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('boat_census:districts'))
    context = {'form':form}
    return render(request,'boat_census/add_district.html',context)

def boat_type(request):
    #Show boat types in the Database
    boat_types = BoatType.objects.all()
    context = {'boat_types':boat_types}
    return render(request,'boat_census/boat_types.html',context)

def boat_classes(request):
    #Show boat classes in the Database
    boat_classes = BoatClass.objects.all()
    context = {'boat_classes':boat_classes}
    return render(request,'boat_census/boat_classes.html',context)
def boat_uses(request):
    #Show boat uses in the Database
    boat_uses = BoatUse.objects.all()
    context = {'boat_uses':boat_uses}
    return render(request,'boat_census/boat_uses.html',context)
def fuel_types(request):
    #Show boat uses in the Database
    fuel_types = FuelType.objects.all()
    context = {'fuel_types':fuel_types}
    return render(request,'boat_census/fuel_types.html',context)
def add_boat_type(request):
    #Enable Users to add boat types
    if request.method != 'POST':
        #Form has not been submitted, present a new form
        form = BoatTypeForm()
    else:
        #Form has been submitted, process data
        form = BoatTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('boat_census:boat_types'))
    context = {'form':form}
    return render(request,'boat_census/add_boat_type.html',context)
def add_boat_class(request):
    #Enable Users to add boat classes
    if request.method != 'POST':
        #Form has not been submitted, present a new form
        form = BoatClassForm()
    else:
        #Form has been submitted, process data
        form = BoatClassForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('boat_census:boat_classes'))
    context = {'form':form}
    return render(request,'boat_census/add_boat_class.html',context)
def add_boat_use(request):
    #Enable Users to add boat uses
    if request.method != 'POST':
        #Form has not been submitted, present a new form
        form = BoatUseForm()
    else:
        #Form has been submitted, process data
        form = BoatUseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('boat_census:boat_uses'))
    context = {'form':form}
    return render(request,'boat_census/add_boat_use.html',context)

def add_fuel_type(request):
    #Enable Users to add fuel types
    if request.method != 'POST':
        #Form has not been submitted, present a new form
        form = FuelTypeForm()
    else:
        #Form has been submitted, process data
        form = FuelTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('boat_census:fuel_types'))
    context = {'form':form}
    return render(request,'boat_census/add_fuel_type.html',context)

def vessels_per_owner(request,owner_id):
    owner = Owner.objects.get(id=owner_id)
    vessels = Vessel.objects.filter(owner=owner)
    context = {'vessels':vessels,'owner':owner}
    return render(request,'boat_census/vessels_per_owner.html',context)

def vessels_per_user(request,user_id):
    user = User.objects.get(id=user_id)
    vessels = Vessel.objects.filter(entrant=user)
    context = {'vessels':vessels,'user':user}
    return render(request,'boat_census/vessels_per_user.html',context)

def sites_per_district(request,district_id):
    district = District.objects.get(id=district_id)
    sites = LandingSite.objects.filter(district=district)
    context = {'sites':sites,'district':district}
    return render(request,'boat_census/landingsites_per_district.html',context)

def add_vessel(request,owner_id):
    owner = Owner.objects.get(id=owner_id)
    
    if request.method != 'POST':
        #form has not been submitted, present a new form 
        form = VesselForm()
    else: 
        form = VesselForm(request.POST)
        if form.is_valid():
            new_vessel = form.save(commit=False)
            new_vessel.entrant = request.user
            new_vessel.owner = owner
            new_vessel.save()
            return HttpResponseRedirect(reverse('boat_census:vessels_per_owner',args=[owner_id]))

    context = {'form':form,'owner':owner}
    return render(request,'boat_census/add_vessel.html',context)

def add_site(request,district_id):
    district = District.objects.get(id=district_id)
    
    if request.method != 'POST':
        #form has not been submitted, present a new form 
        form = LandingSiteForm()
    else: 
        form = LandingSiteForm(request.POST)
        if form.is_valid():
            new_site = form.save(commit=False)
            new_site.district = district
            new_site.save()
            return HttpResponseRedirect(reverse('boat_census:sites_per_district',args=[district_id]))

    context = {'form':form,'district':district}
    return render(request,'boat_census/add_site.html',context)