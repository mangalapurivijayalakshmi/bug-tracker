from django import forms
from bugs.models import *

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'priority', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }