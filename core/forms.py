from django import forms
from .models import *



class TodoForm(forms.ModelForm):
    
    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('complete', 'Complete'),
    )

    
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ 'class':'form-control', 'placeholder': 'Task Title'}) ,label="Title")
    
    task_details = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class':'form-control ','placeholder': 'Task Details'}) ,label="Details of Task")
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    due_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={'class':'form-control ','placeholder': '','type':'date'}), label="Due date")
    
    class Meta:
        model = Todo
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextField(attrs={'class':'form-control'}),
        # }