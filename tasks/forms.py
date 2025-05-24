from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title', 'completed', 'priority', 'due_date']
        widgets={
            'due_date':forms.DateInput(
                attrs={
                    'placeholder':'YYYY-MM-DD',
                    'type':'date'
                }
            )
        }