from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')

# Recebendo ID 
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')

