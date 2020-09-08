from django import forms

from .models import Task


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'user',
            'day_of_the_week',
            'site_name',
            'contract_number',
            'duration',
            'description',
            'car_reg',
        ]

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'day_of_the_week': forms.Select(attrs={'class': 'form-control'}),
            'site_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_number': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'car_reg': forms.Select(attrs={'class': 'form-control'}),
        }

        
