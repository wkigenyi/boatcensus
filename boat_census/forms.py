from django import forms 
from .models import Owner,District,BoatType,BoatUse,BoatClass,FuelType,Propulsion,Vessel,LandingSite,BoatClass,Color

class OwnerForm(forms.ModelForm):
    #Enable Users to add owners
    class Meta:
        model = Owner
        fields = ['name','national_id','driver_license','tel1','tel2','tel3','tel4']
        labels = {'name':'Owner Name'}

class DistrictForm(forms.ModelForm):
    #Enable Addition Of Districts
    class Meta:
        model = District
        fields = ['district_name']

class BoatTypeForm(forms.ModelForm):
    #Enable Addition Of Boat Types
    class Meta:
        model = BoatType
        fields = ['boat_type']
class BoatUseForm(forms.ModelForm):
    #Enable Addition Of Boat Use
    class Meta:
        model = BoatUse
        fields = ['boat_use']
class BoatClassForm(forms.ModelForm):
    #Enable Addition Of Boat Class
    class Meta:
        model = BoatClass
        fields = ['boat_class']
class FuelTypeForm(forms.ModelForm):
    #Enable Addition Of Fuel Type
    class Meta:
        model = FuelType
        fields = ['fuel_name']
class PropulsionForm(forms.ModelForm):
    #Enable Addition Of Propulsion
    class Meta:
        model = Propulsion
        fields = ['prop_name']
        labels = {'prop_name':'Propulsion Name'}

class VesselForm(forms.ModelForm):
    #Enable Addition Of Vessels
    class Meta:
        model = Vessel
        exclude = ['entrant','owner']
        widgets = {'census_date':forms.TextInput(attrs={'type':'date'})}
        
class LandingSiteForm(forms.ModelForm):
    #Enable Addition Of Landing Sites
    class Meta:
        model = LandingSite
        exclude = ['district']
class BoatClassForm(forms.ModelForm):
    #Enable Addition Of Classes
    class Meta:
        model = BoatClass
        fields = ['boat_class']
class BoatUseForm(forms.ModelForm):
    #Enable Addition Of Boat Uses
    class Meta:
        model = BoatUse
        fields = ['boat_use']

class ColorForm(forms.ModelForm):
    #Enable Addition Of Color
    class Meta:
        model = Color
        fields = ['color']
        
        