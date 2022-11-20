from django.shortcuts import render
from . models import Project, Profile
 

def home(request):
    projects = Project.objects.all()
    profile = Profile.objects.all()
    context = {'projects': projects, 'profile': profile}
    return render(request, 'base\home.html', context)

def project_detail(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'base\project_detail.html', {'project': projectObj, 'tags': tags})