from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def historia(request):
    return render(request, 'core/historia.html')

def visitanos(request):
    return render(request, 'core/visitanos.html')

