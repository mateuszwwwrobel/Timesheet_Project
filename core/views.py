from django.shortcuts import render
from .forms import AddJobForm
from .models import Task

# Create your views here.

def landing_page_view(request):
    
    return render(request, 'landing_page.html')


def week_view(request):
    context = {
        'week_tasks': Task.objects.all(),

    }
    return render(request, 'week_page.html', context)



def add_job_view(request):
    form = AddJobForm(request.POST or None)
    
    context = {
     
        'form': form
    }

    return render(request, 'add_job_form.html', context)


def save_job(request):
    form = AddJobForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    return render(request, 'job_added.html')