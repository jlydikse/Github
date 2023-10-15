from django.shortcuts import render
from django.db import models


# Create your views here.
def myview(request):
    return render(request, "index.html")

class Thread(models.Model):
    title = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
