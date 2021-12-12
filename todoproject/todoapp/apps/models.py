from django.db import models


# Create your models here.

class Todo(models.Model):
    Priorities = [
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    ]
    task = models.CharField(max_length=200)
    priority = models.CharField(max_length=20, choices = Priorities)
    date_joined = models.DateTimeField(auto_now_add=True)
    explanation = models.TextField()
    
    
    def __str__(self):
        return self.task
    