from django.shortcuts import render, redirect
from .forms import ProduktForm
from rest_framework import viewsets
from .models import Produkt
from .serializers import ProduktSerializer

def lista_zakupow(request):
    produkty = Produkt.objects.all()

    if request.method == 'POST':
        form = ProduktForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_zakupow')
    else:
        form = ProduktForm()

    return render(request, 'PI_MVC/shopping_list.html', {'produkty': produkty, 'form': form})


class ProduktViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer