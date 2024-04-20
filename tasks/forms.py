from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    """
    Formulario para el modelo Task.
    
    Este formulario permite crear, editar y validar instancias del modelo Task.
    """

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "price": forms.NumberInput(attrs={'class': 'custom-input'}),
            'stock': forms.NumberInput(attrs={'class': 'custom-input'}),
            'status': forms.Select(attrs={'class': 'custom-input'}),
            'actives': forms.Select(attrs={'class': 'custom-input'}),
        }

class QuantityForm(forms.Form):
    """
    Formulario para la cantidad a comprar.
    
    Este formulario permite al usuario ingresar la cantidad de un producto que desea comprar.
    """

    quantity = forms.IntegerField(min_value=1)


