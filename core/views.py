from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .forms import AddJobForm
from .models import Task, UserTask
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


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
    
    def delete_job(self):
        user = self.request.user

        

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
        full_tasks = UserTask(weekly_tasks)
        
        print(full_tasks)
        weekly_tasks.delete()

        return render(self.request, 'reset_timesheet.html')

    

@login_required
def delete_single_job_from_week(request):
    user = request.user

    try: 
        deleted_job = Task.objects.get(user=user)
        deleted_job.delete()
        return redirect('core:week-page-view')

    except ObjectDoesNotExist:

        return redirect('core:week-page-view')


@login_required
def total_hours(request):
    user = request.user

    duration = Task.objects.filter(user=user)
    try: 
        total_h = Task.objects.get(duration=duration)
        print(total_h)
        return total_h
    except ObjectDoesNotExist:
        return redirect('core:week-page-view') 
    
