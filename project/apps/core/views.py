from django.shortcuts import render

def index(request):
    context = {"app_name": "Spiderweb"}
    return render(request, "core/index.html",context)

def about(request):
    return render(request, 'core/about.html')

