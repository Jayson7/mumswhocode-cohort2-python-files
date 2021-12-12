from django.shortcuts import render
from .models import Todo
# Create your views here.
'''
types of views 
# function base views (fbv)
# class base views (cbv)
'''

# read
def homepage(request):
    todo = Todo.objects.all()    
    context ={}
    context['todos'] = todo
    return render(request, 'index.html', context)


# create
def createTask(request):
    context ={}
    
    return render(request, 'createtask.html', context)

# update
def updateTask(request):
    context ={}
    
    return render(request, 'updatetask.html', context)

#delete 
def deleteTask(request):
    context ={}
    
    return render(request, 'deletetask.html', context)