from django.urls import path

from Recipes import views

urlpatterns = [
    path('', views.sobre),
    path('contact/', views.contact)
]
