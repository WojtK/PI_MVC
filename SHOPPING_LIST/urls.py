"""
URL configuration for PI_MVC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django_distill import distill_path
from rest_framework.routers import DefaultRouter
from .views import ProduktViewSet, ListaZakupowView

router = DefaultRouter()
router.register(r'produkty', ProduktViewSet)

urlpatterns = [
    distill_path('', ListaZakupowView.as_view(), name='lista_zakupow', distill_file='shopping_list.html'),
]
