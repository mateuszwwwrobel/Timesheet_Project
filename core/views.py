from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.views.generic import View
from .forms import AddJobForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import csv, datetime, io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.contrib.auth.models import User
import os



# Create your views here.

def landing_page_view(request):
    return render(request, 'landing_page.html')


class WeekView(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        
        context = {
        'week_tasks': Task.objects.filter(user=user),
        'total_hours': Task.objects.filter(user=user).aggregate(Sum('duration'))['duration__sum'],
        }

        return render(self.request, 'week_page.html', context)

        
@login_required
def add_job_view(request):
    user = request.user
    form = AddJobForm(request.POST or None, initial={'user': user})
    
    context = {
     
        'form': form
    }

    return render(request, 'add_job_form.html', context)

@login_required
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


""" def hello(c):
    #Basic information about user
    #user = Task.objects.filter(user=user)
    user = "Matt"
    date = str(datetime.datetime.now().day) +'.' + str(datetime.datetime.now().month) + '.' + str(datetime.datetime.now().year)

    #Headline with user name and week ending date
    c.setFont("Helvetica", 14)
    c.drawString(30,750,"Timesheet")
    c.setFont("Helvetica", 12)
    c.drawString(30,770,"Week ending date   " + date)
    c.drawString(120,750,user)

    #Borders, table-like view:
    c.translate(25,785)
    c.rect(0,0,550,-738,1,0)
    c.translate(107,0)
    c.line(0,0,0,-20)
    c.translate(-107,-20)
    c.line(0,0,550,0)
    c.translate(0,-20)
    c.line(0,0,550,0) """


@login_required
def export_week_to_file(request):
    user = request.user
    response = HttpResponse(content_type='text/csv')
    date = str(datetime.datetime.now().day) +'.' + str(datetime.datetime.now().month) + '.' + str(datetime.datetime.now().year)
    file_name = str(user) + ' ' + str(date)
    response['Content-Disposition'] = 'attachment; filename="Timesheet - %s.csv"' % file_name
    file_path = os.path.join(os.path.expanduser("~"), "Desktop/", file_name)

    #c = canvas.Canvas(file_path ,file_name)
    #hello(c)
    #c.showPage()
    #c.save()
    
    writer = csv.writer(response)
    writer.writerow(['Date', 'Site name', 'Contract number', 'Hours', 'Description', 'Car registration'])
    for task in Task.objects.filter(user=user).values_list('date', 'site_name', 'contract_number', 'duration', 'description', 'car_reg'):
        writer.writerow(task)

    return response


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/week/')

    return redirect('/week/')
    
