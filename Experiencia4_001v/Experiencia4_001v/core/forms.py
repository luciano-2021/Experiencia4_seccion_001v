from django import forms 
from django.forms import ModelForm, widgets
from .models import Proveedores, Tipomaterial


class ProveedoresForm(ModelForm): 

    class Meta: 
        model = Proveedores 
        fields = ['ididentificacion','nombrecompleto','Telefono','direccion','email','pais','monedadepago','tipomaterial']

        labels={
            'ididentificacion': 'Digite id del proveedor',
            'nombrecompleto': 'Digite nombre completo',
            'Telefono': 'Telefono',
            'direccion': 'direccion',
            'email': 'email', 
            'pais': 'pais',
            'moneda de pago': 'monedadepago',
            'tipomaterial' : 'tipomaterial'
        }

        widgets={
            'ididentificacion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'ididentificacion', 
                    'id': 'txtididentificacion'
                }
            ),

            'nombrecompleto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'nombrecompleto', 
                    'id': 'txtnombrecompleto'
                }
            ),
            'Telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Telefono', 
                    'id': 'txtTelefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'direccion', 
                    'id': 'txtdireccion'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'email', 
                    'id': 'txtemail'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'pais', 
                    'id': 'txtpais'
                }
            ),
            'monedadepago': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'moneda de pago', 
                    'id': 'txtmonedadepago'
                }
            ),
            'tipomaterial': forms.Select(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'tipomaterial', 
                    'id': 'txttipomaterial'
                }
            ),
        }
