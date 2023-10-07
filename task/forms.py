from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','body']
        widgets={
            'title':forms.TextInput(attrs={
                'placeholder':'Enter a title for the task',
                'class':'w-full border border-gray-700 px-6 py-4 rounded-lg'
            }),
            'body':forms.Textarea(attrs={
                'placeholder':'Description about the task',
                'class':'h-48 w-full border border-solid border-gray-700 rounded-lg mb-2 px-6 py-6'
            })
        }