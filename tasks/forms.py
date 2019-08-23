from django import forms
from .models import Task



class Date(forms.DateInput): # Date input widget
    input_type = 'date'

class Time(forms.TimeInput): #Time input widget
    input_type = 'time'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {'task_date': Date(), 'task_time': Time()}
        fields = ['title', 'details', 'task_date', 'task_time']
