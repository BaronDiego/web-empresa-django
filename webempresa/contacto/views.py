from django import forms
from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.urls import reverse

# Create your views here.

def contacto(request):
   
    formulario = ContactoForm()
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('nombre', '')
            email = request.POST.get('email', '')
            contenido = request.POST.get('contenio', '')
            return redirect(reverse('contacto')+'?ok')

    return render(request, 'contacto/contacto.html', {'formulario':formulario})