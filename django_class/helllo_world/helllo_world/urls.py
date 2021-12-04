from apps import views 
from apps.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Hompage, name="home")
]
