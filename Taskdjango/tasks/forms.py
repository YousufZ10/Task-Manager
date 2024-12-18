from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_number', 'task_name', 'task_description', 'task_deadline_date', 'task_status']
        labels = {
            'task_number': 'Task Number',
            'task_name': 'Task Name',
            'task_description': 'Description',
            'task_deadline_date': 'Deadline',
            'task_status': 'Status',
        }
        widgets = {
            'task_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'task_description': forms.Textarea(attrs={'class': 'form-control'}),
            'task_deadline_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'task_status': forms.Select(attrs={'class': 'form-control'}),
        }
