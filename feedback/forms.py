from django import forms
from django.forms.widgets import NumberInput
import datetime


problems = [
    ('', 'Select a topic of feedback'),
    ('Interface', 'Interface'),
    ('Product', 'Product'),
    ('Delivery', 'Delivery'),
    ('Packaging', 'Packaging'),
]


class feedbackForm(forms.Form):
    name  = forms.CharField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    fdate = forms.DateField(
        widget=NumberInput(attrs={'type': 'date', 'style' : 'display:none'}),
        initial=datetime.date.today,
        label="")
    type = forms.ChoiceField(choices=problems)
    file = forms.FileField(label="Add an image of problem")
    terms = forms.BooleanField(label="Agree to terms and condition:")