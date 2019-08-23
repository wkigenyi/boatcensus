from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',views.logout_user,name='logout'),
]