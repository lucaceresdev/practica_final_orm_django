from django.shortcuts import render, redirect
from laboratorio.models import Laboratorio  # Importa el modelo 'Laboratorio' con mayúscula inicial

def list_laboratorios(request):
    laboratorios = Laboratorio.objects.all()  # Utiliza el modelo 'Laboratorio' con mayúscula inicial
    return render(request, 'list_laboratorios.html', {'laboratorios': laboratorios})

def create_laboratorio(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)  # Utiliza el modelo 'Laboratorio' con mayúscula inicial
        laboratorio.save()
        return redirect('list_laboratorios')
    return render(request, 'create_laboratorio.html')

def update_laboratorio(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)  # Utiliza el modelo 'Laboratorio' con mayúscula inicial
    if request.method == 'POST':
        laboratorio.nombre = request.POST['nombre']
        laboratorio.ciudad = request.POST['ciudad']
        laboratorio.pais = request.POST['pais']
        laboratorio.save()
        return redirect('list_laboratorios')
    return render(request, 'update_laboratorio.html', {'laboratorio': laboratorio})

def delete_laboratorio(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)  # Utiliza el modelo 'Laboratorio' con mayúscula inicial
    laboratorio.delete()
    return redirect('list_laboratorios')
