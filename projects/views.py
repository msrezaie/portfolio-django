from django.shortcuts import render
from . models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects_list.html', context)

def project_detail(request, pk):
    projects = Project.objects.get(id=pk)
    context = {'projects' : projects}
    return render(request, 'projects_detail.html', context)