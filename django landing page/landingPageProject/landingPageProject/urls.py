
from django.contrib import admin
from django.urls import path
from landingApp import views
from landingApp.views import homepage


urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('', views.homepage)
    
]
