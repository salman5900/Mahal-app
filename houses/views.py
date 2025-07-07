from django.shortcuts import render
from .models import Hosuse

# Create your views here.
def houses(request):
    houses = Hosuse.objects.all().order_by('-date_posted')
    context = {
        'houses': houses,
        'transparent_nav': False,
    }
    return render(request, 'Houses/houses.html', context)