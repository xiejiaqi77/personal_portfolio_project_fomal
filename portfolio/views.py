from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all() #grab all the projects in the
    return render(request, 'portfolio/Home.html', {'projects': projects})

def projects(request):
    projects = Project.objects.all()  # grab all the projects in the
    return render(request, 'portfolio/Projects.html', {'projects': projects})