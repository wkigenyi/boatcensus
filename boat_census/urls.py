from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name= 'index'),
    path('owners/',views.owners_view,name='owners'),
    path('districts/',views.districts,name='districts'),
    path('boat_types/',views.boat_type,name='boat_types'),
    path('boat_classes/',views.boat_classes,name='boat_classes'),
    path('boat_uses/',views.boat_uses,name='boat_uses'),
    path('colors/',views.colors,name='colors'),
    path('fuel_types/',views.fuel_types,name='fuel_types'),
    path('enumerators/',views.enumerators,name='enumerators'),
    path('add_enumerator/',views.add_enumerator,name='add_enumerator'),
    path('propulsion_types/',views.prop_types,name='prop_types'),
    path('hull_material/',views.hull_material,name='hull_material'),
    path('add_hull_material/',views.add_hull_material,name='add_hull_material'),
    path('add_owner/',views.add_owner,name='add_owner'),
    path('add_district/',views.add_district,name='add_district'),
    path('add_color/',views.add_color,name='add_color'),
    path('add_boat_type/',views.add_boat_type,name='add_boat_type'),
    path('add_prop_type/',views.add_prop_type,name='add_prop_type'),
    path('add_boat_use/',views.add_boat_use,name='add_boat_use'),
    path('add_fuel_type/',views.add_fuel_type,name='add_fuel_type'),
    path('add_boat_class/',views.add_boat_class,name='add_boat_class'),
    path('vessels/<int:owner_id>/',views.vessels_per_owner,name='vessels_per_owner'),
    path('add_vessel/<int:owner_id>/',views.add_vessel,name='add_vessel'),
    path('vessels/',views.vessels,name='vessels'),
    path('vesselz/<int:user_id>/',views.vessels_per_user,name='vessels_per_user'),
    path('sites/<int:district_id>/',views.sites_per_district,name='sites_per_district'),
    path('add_site/<int:district_id>/',views.add_site,name='add_site'),
]