from django.shortcuts import render, redirect, get_object_or_404
from .models import Produkt
from .forms import ProduktForm


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


def usuwanie_produktu(request, produkt_id):
    produkt = Produkt.objects.get(id=produkt_id)
    produkt.delete()
    return redirect('lista_zakupow')


def edycja_produktu(request, produkt_id):
    produkt = get_object_or_404(Produkt, id=produkt_id)

    if request.method == 'POST':
        form = ProduktForm(request.POST, instance=produkt)
        if form.is_valid():
            form.save()
            return redirect('lista_zakupow')
    else:
        form = ProduktForm(instance=produkt)

    return render(request, 'PI_MVC/edit.html', {'form': form, 'produkt': produkt})