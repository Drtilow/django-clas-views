from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def zobraz_parametr(request):
    parametr = request.GET.get('moj_param', 'nic nevyplněno')
    return HttpResponse(f"Parametr je: {parametr}")

def vyber_kategorii(request):
    vybrana_kategorie = None
    if request.method == 'POST':
        vybrana_kategorie = request.POST.get('kategorie')
    return render(request, 'vyber_kategorie.html', {'kategorie': vybrana_kategorie})

def zpetna_vazba(request):
    uspesne = False
    if request.method == 'POST':
        jmeno = request.POST.get('jmeno')
        zprava = request.POST.get('zprava')
        print(f"Jméno: {jmeno}, Zpráva: {zprava}")
        uspesne = True
    return render(request, 'zpetna_vazba.html', {'uspesne': uspesne})

class KontaktView(View):
    def get(self, request):
        return render(request, 'kontakt.html')

    def post(self, request):
        jmeno = request.POST.get('jmeno')
        zprava = request.POST.get('zprava')
        print(f"Jméno: {jmeno}, Zpráva: {zprava}")
        return render(request, 'kontakt.html', {'potvrzeni': True})