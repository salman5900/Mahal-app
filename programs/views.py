from django.shortcuts import render
from programs.models import Programs
# Create your views here.
def programs(request):
    program = Programs.objects.all().order_by('-date_posted')
    context = {
        'transparent_nav': False,
        'programs': program,    
    }
    return render(request, 'programs/programs.html', context)

def program_detail(request, program_id):
    program = Programs.objects.get(id=program_id)
    context = {
        'transparent_nav': False,
        'program': program,
    }
    return render(request, 'programs/program_detail.html', context)