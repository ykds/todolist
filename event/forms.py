from django import forms

from event.models import Event
from .models import Event

class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'content')
        widgets = {
            'content': forms.Textarea(attrs={'cols':80, 'rows': 10}),
        }

