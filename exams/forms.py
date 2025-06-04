from django import forms
from .models import HallAllocation

class HallAllocationForm(forms.ModelForm):
    class Meta:
        model = HallAllocation
        fields = ['student', 'exam', 'exam_hall', 'allocation_date', 'allocation_time']
