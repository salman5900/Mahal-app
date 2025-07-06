from django.shortcuts import render

# Create your views here.
def houses(request):
    return render(request, 'Houses/houses.html',{"transparent_nav": False})