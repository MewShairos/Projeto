from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]

# UrlsDinâmicas: <id> funciona como parâmetro, passando para a view. Já ":int"