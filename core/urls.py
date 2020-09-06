from django.urls import path
from .views import week_view, landing_page_view, add_job_view, save_job

app_name = 'core'


urlpatterns = [
    path('', landing_page_view, name='landing-page-view'),
    path('add-job/', add_job_view, name='add-job-page-view'),
    path('week/', week_view, name='week-page-view'),
    path('job-added', save_job, name='save_job')