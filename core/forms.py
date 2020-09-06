from django import forms

from .models import Task


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'user',
            'day_of_the_week',
            'duration',
            'contract_number',
            'description',
            'car_reg',
        ]

        labels = {
            
        }

        widgets = {

        }