from django.contrib import admin
from django.urls import path

# views configuration 
from apps import views 
from apps.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'  )  # url config for homepage
]
