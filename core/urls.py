from django.urls import path
from .views import landing_page_view, add_job_view, save_job, WeekView, ResetTimesheet

app_name = 'core'


urlpatterns = [
    path('', landing_page_view, name='landing-page-view'),
    path('add-job/', add_job_view, name='add-job-page-view'),
    path('week/', WeekView.as_view(), name='week-page-view'),
    path('job-added', save_job, name='save_job'),
    path('reset-timesheet', ResetTimesheet.as_view(), name='reset-timesheet'),

]