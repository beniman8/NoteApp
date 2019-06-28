from django import forms
from .models import Note

class NoteModelForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ("title",'due_date','label')

    title= forms.CharField(widget = forms.TextInput(
        attrs={
            'placeholder': 'Title',
            'class': 'form-control'
        }
    ))
    due_date= forms.CharField(widget = forms.TextInput(
        attrs={
            'placeholder': 'Due Date',
            'class': 'form-control'
            
        }
    ))
    
