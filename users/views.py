from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate

# Create your views here.
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('boat_census:index'))
