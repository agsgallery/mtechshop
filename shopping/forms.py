from django import forms
from .models import order


class DateInput(forms.DateInput):
    input_type = 'date'

class orderform(forms.ModelForm):
    class Meta:
        model=order
        fields='__all__'
        widgets={
            'orderdate': DateInput(),
        }