from django.shortcuts import render


def sobre(request):
    return render(request, 'recipes/home.html', context={"name": "Iuri"})

def contact(request):
    return render(request, 'temp/temp.html', context={"name": "Iuri"})
