from django import forms

from .models import Task


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'user',
            'date',
            'site_name',
            'contract_number',
            'duration',
            'description',
            'car_reg',
        ]

        widgets = {
            'user': forms.HiddenInput(attrs={'class': 'form-control small-tab'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'site_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_number': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'car_reg': forms.Select(attrs={'class': 'form-control'}),
        }

        
