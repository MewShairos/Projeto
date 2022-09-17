from django.http import HttpResponse


def sobre(request):
    return HttpResponse("SOBRE")

def contato(request):
    return HttpResponse("CONTATO")

def home(request):
    return HttpResponse("HOME")
