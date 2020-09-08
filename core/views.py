from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from .forms import AddJobForm
from .models import Task, UserTask

# Create your views here.

def landing_page_view(request):
    
    return render(request, 'landing_page.html')



class WeekView(View):
    def get(self, *args, **kwargs):
        user = self.request.user

        context = {
        'week_tasks': Task.objects.filter(user=user),
        }

        return render(self.request, 'week_page.html', context)



def add_job_view(request):
    user = request.user
    form = AddJobForm(request.POST or None, initial={'user': user})
    
    context = {
     
        'form': form
    }

    return render(request, 'add_job_form.html', context)


def save_job(request):
    form = AddJobForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'job_added.html')


class ResetTimesheet(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        weekly_tasks = Task.objects.filter(user=user)
        weekly_tasks.delete()

        return render(self.request, 'reset_timesheet.html')
