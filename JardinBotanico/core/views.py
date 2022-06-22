from django.shortcuts import render

# Create your views here.
# Create your views here.
# Crea tus vistas Aqui

def home(request):
    return render(request, 'core/index.html')