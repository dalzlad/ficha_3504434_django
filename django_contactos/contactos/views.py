from django.shortcuts import render
from .models import Contacto

# Create your views here.
def crear(request):
    if request.method == "POST":
        contacto = Contacto(
            nombre = request.POST["nombre"],
            correo = request.POST["correo"],
            telefono = request.POST["telefono"],
            mensaje = request.POST["mensaje"]
        )

        contacto.save() #Guardar el contacto
    return render(request, "formulario.html")

#Método para listar los datos del contacto
def listar(request):
    #Traer todos los registros de la tabla contactos. #Select * from contactos
    contactos = Contacto.objects.all()
    return render(
        request,
        "lista.html",
        {"contactos":contactos}
    )