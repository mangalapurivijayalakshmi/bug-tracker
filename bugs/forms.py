from django import forms
from bugs.models import Bug


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter bug title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe the bug in detail'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title.strip():
            raise forms.ValidationError("Title cannot be empty")
        return title


class BugEditForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'priority', 'status', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),
        }
