
from django.contrib import admin
from django.urls import path
from apps.views import *
from apps import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('create', views.createTask, name="create"),
    path('update/<int:pk>', views.updateTask, name="update"),
    path('delete/<int:pk>', views.deleteTask, name="delete"),
]
