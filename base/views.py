from django.shortcuts import render
from . models import Project
 

def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'base\home.html', context)

def project_detail(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'base\project_detail.html', {'project': projectObj})