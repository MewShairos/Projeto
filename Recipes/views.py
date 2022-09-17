from django.shortcuts import render


def sobre(request):
    return render(request, 'recipes/pages/home.html', context={"name": "Iuri"})
