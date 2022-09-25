from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]

# UrlsDinâmicas: <id> funciona como parâmetro, passando para a view. Já ":int"