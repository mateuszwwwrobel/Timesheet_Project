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

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'day_of_the_week': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'contract_number': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'car_reg': forms.TextInput(attrs={'class': 'form-control'}),
        }

        
