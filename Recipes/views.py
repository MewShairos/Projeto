from django.shortcuts import render


def sobre(request):
    return render(request, 'recipes/home.html')
