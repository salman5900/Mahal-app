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

def house_detail(request, house_id):
    house = Hosuse.objects.get(id=house_id)
    context = {
        'house': house,
        'transparent_nav': False,
    }
    return render(request, 'Houses/house_detail.html', context)