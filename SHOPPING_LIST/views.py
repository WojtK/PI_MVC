from django.shortcuts import render, redirect
from django.views import View

from .forms import ProduktForm
from rest_framework import viewsets
from .models import Produkt
from .serializers import ProduktSerializer


class ListaZakupowView(View):
    template_name = 'PI_MVC/shopping_list.html'

    def get(self, request):
        produkty = Produkt.objects.all()
        form = ProduktForm()
        return render(request, self.template_name, {'produkty': produkty, 'form': form})

    def post(self, request):
        form = ProduktForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_zakupow')

        produkty = Produkt.objects.all()
        return render(request, self.template_name, {'produkty': produkty, 'form': form})


class ProduktViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer