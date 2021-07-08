from django.shortcuts import render, redirect
from .models import Tipomaterial, Proveedores
from .forms import ProveedoresForm

# Create your views here.
#solicitud a servidor
def home(request):   

    return render (request, 'home.html')

def proveedores(request):
    if request.method == 'POST':
        proveedores=ProveedoresForm(request.POST)
        if proveedores.is_valid():
            proveedores.save()
            return redirect('Proveedores')
    else:
        proveedores=ProveedoresForm()
        listaProveedores = Proveedores.objects.all()

    return render (request, 'core/proveedores.html', {'proveedores': proveedores, 'listaProveedores':listaProveedores})
   



def editaProveedores(request, ididentificacion):  
    proveedor = Proveedor.objects.get(ididentificacion=ididentificacion)

    datos={ 
        'form':ProveedoresForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = ProveedoresForm(data=request.POST, instance = proveedor)
        if formulario.is_valid:
            formulario.save()
            return redirect('proveedores')

    return render (request, 'core/editaProveedor.html', datos)

def eliminaProveedor(request, ididentificacion):
    proveedor = Proveedor.objects.get(ididentificacion=ididentificacion)
    proveedor.delete()
    return redirect('proveedores')

