from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def citas(request):
    return render(request, 'citas.html')

def contacto(request):
    return render(request, 'contacto.html')

def cortes(request):
    return render(request, 'cortes.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
