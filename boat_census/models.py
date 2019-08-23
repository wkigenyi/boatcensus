from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class District (models.Model):
    district_name = models.CharField(max_length=200)

    def __str__(self):
        return self.district_name

class FuelType (models.Model):
    fuel_name = models.CharField(max_length=200)
    def __str__(self):
        return self.fuel_name
class BoatClass (models.Model):
    boat_class = models.CharField(max_length=200)

    def __str__(self):
        return self.boat_class

class Propulsion (models.Model):
    prop_name = models.CharField(max_length=200)
    def __str__(self):
        return self.prop_name

class BoatUse (models.Model):
    boat_use = models.CharField(max_length=200)

    def __str__(self):
        return self.boat_use

class HullMaterial(models.Model):
    hull_material = models.CharField(max_length=200)

    def __str__(self):
        return self.hull_material

class Color (models.Model):
    color = models.CharField(max_length=200)
    def __str__(self):
        return self.color

class BoatType (models.Model):
    boat_type = models.CharField(max_length=200)
    def __str__(self):
        return self.boat_type

class BoatBuilder (models.Model):
    boat_builder = models.CharField(max_length=200)
    def __str__(self):
        return self.boat_builder

class LandingSite(models.Model):
    site_name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self):
        return self.site_name

class Owner(models.Model):
    name = models.CharField(max_length=200)
    national_id = models.CharField(max_length = 200,blank=True)
    driver_license = models.CharField(max_length = 200,blank=True)
    tel1 = models.CharField(max_length=200,blank=True)
    tel2 = models.CharField(max_length=200,blank=True)
    tel3 = models.CharField(max_length=200,blank=True)
    tel4 = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.name
class Enumerator(models.Model):
    surname_name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    tel1 = models.CharField(max_length=200)
    tel2 = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.surname_name+" "+self.other_name


class Vessel(models.Model):
    vessel_number = models.CharField(max_length=200)
    vessel_name = models.CharField(max_length=200)
    landing_site = models.ForeignKey(LandingSite,on_delete=models.CASCADE)
    boat_class = models.ForeignKey(BoatClass,on_delete=models.CASCADE)
    life_jackets = models.IntegerField()
    life_rings = models.IntegerField()
    passenger_capacity = models.IntegerField()
    cargo_capacity = models.DecimalField(decimal_places=2,max_digits=4)
    hull_id = models.CharField(max_length=200)
    width = models.DecimalField(decimal_places=2,max_digits=4)
    length = models.DecimalField(decimal_places=2,max_digits=4)
    year_of_build = models.CharField(max_length=4,null=True)
    boat_type = models.ForeignKey(BoatType,null=True,on_delete=models.CASCADE)
    propulsion = models.ForeignKey(Propulsion,null=True,on_delete=models.CASCADE)
    boat_use = models.ForeignKey(BoatUse,null=True,on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(FuelType,null=True,on_delete=models.CASCADE)
    hull_material = models.ForeignKey(HullMaterial,null=True,on_delete=models.CASCADE)
    hull_color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,related_name='hullcolor')
    cabin_color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,related_name='cabincolor')
    owner = models.ForeignKey(Owner,null=True,on_delete=models.CASCADE)
    census_date = models.DateField(null=True) 
    enumerator = models.ForeignKey(Enumerator,null=True,on_delete=models.CASCADE) 
    entrant = models.ForeignKey(User, on_delete=models.CASCADE)  
    def __str__(self):
        return self.vessel_number