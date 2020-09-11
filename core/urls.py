from django.urls import path
from .views import landing_page_view, add_job_view, save_job, WeekView, ResetTimesheet, delete_single_job_from_week, total_hours

app_name = 'core'


urlpatterns = [
    path('', landing_page_view, name='landing-page-view'),
    path('add-job/', add_job_view, name='add-job-page-view'),
    path('week/', WeekView.as_view(), name='week-page-view'),
    path('job-added', save_job, name='save_job'),
    path('reset-timesheet', ResetTimesheet.as_view(), name='reset-timesheet'),
    path('delete-single-job', delete_single_job_from_week, name='delete_single_job_from_week'),
    path('total_hours', total_hours, name='total_hours'),



]