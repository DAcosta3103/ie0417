from django.http import HttpResponse  # <-- Importar HttpResponse

def home(request):
    return HttpResponse("¡Hola desde lab5-docker-django con Docker y Django!")
