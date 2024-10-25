from django import forms
from .models import task

class taskFrom(forms.ModelForm):
    class Meta:
        model = task
        fields = '__all__'
        # fields = ['name', 'bio']
        # exclude = ['bio']
        widgets = {
            'category': forms.CheckboxSelectMultiple,
        }