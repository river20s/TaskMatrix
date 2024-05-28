from django import forms
from .models import Task, TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'urgency', 'importance']

class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['name']
