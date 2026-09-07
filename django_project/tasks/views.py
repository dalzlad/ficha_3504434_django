from django.http import	HttpResponse #Libreria para dar respuestas http

def home(request):
    return HttpResponse("Hello, This my first application")