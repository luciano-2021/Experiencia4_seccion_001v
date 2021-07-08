from django.urls import path
from .views import home, proveedores

# llamar a los metodos del veiws.py


urlpatterns = [
    path('home', home, name="home"),
    path('proveedores', proveedores, name="proveedores")
    
    path('editaProveedor<ididentificacion>', editaProveedores, name="editaProveedores"),
    path('eliminaProveedor/<ididentificacion>', eliminaProveedores, name="eliminaProveedores"),

]

