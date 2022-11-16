from django.shortcuts import render
 

def home(request):
    msg = "hello you are on the projects section"
    return render(request, 'base\home.html', {'msg': msg})

def project_detail(request, pk):
    msg = "hello you are on the home page"
    return render(request, 'base\home.html', {'msg': msg})