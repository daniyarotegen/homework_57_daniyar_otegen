from django import forms
from django.core.exceptions import ValidationError
from tracker.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Summary',
            'description': 'Description',
            'status': 'Status',
            'type': 'Type'
        }

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 2:
            raise ValidationError('Summary must be longer than 2 symbols')
        return summary
