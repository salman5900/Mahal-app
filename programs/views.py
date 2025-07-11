from django.shortcuts import render

# Create your views here.
def programs(request):
    context = {
        'transparent_nav': False,
    }
    return render(request, 'programs/programs.html', context)