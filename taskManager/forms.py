from django import forms
from .models import Task
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description'] 
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o título da tarefa'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Digite a descrição da tarefa'}),
        }  

class updateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed'] 
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-control'})
        } 
        
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'completed': 'Concluído'
        }