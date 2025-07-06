from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html',{"transparent_nav": True})