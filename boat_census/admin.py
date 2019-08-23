from django.contrib import admin
from .models import Owner,HullMaterial,BoatType,Color,BoatClass,LandingSite,FuelType,Propulsion,BoatUse,Vessel,Enumerator
# Register your models here.
admin.site.register(Owner)
admin.site.register(HullMaterial)
admin.site.register(BoatClass)
admin.site.register(BoatType)
admin.site.register(Color)
admin.site.register(LandingSite)
admin.site.register(FuelType)
admin.site.register(Propulsion)
admin.site.register(BoatUse)
admin.site.register(Vessel)
admin.site.register(Enumerator)
