from django.shortcuts import render;
from feedback import forms

def Home(request):
    return render(request, 'index.html')

def feedbackform(request):
    form = forms.feedbackForm()
    return render(request, 'feedbackform.html', {'form': form})
    