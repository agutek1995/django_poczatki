from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from datetime import datetime
import random


# Create your views here.
def widok_pierwszej_strony(request):
    with open ('tekst.txt', 'r', encoding='utf8') as f:


        liczba=random.randrange(10)
        dzisiaj=date.today()
        now = datetime.now()
        data = dzisiaj.strftime("%d/%m/%Y")
        godzina = now.strftime("%H:%M:%S")
        print(godzina)
        # return HttpResponse('Witaj na stronie Agaty')
        print('ktoś ogląda moją stronę')
        return render(request, 'szablonAgaty.html', {'dzisiaj':data, 'liczba':liczba, 'godzina':godzina, 'text':f.read()})

def widok_drugiej_strony(request):

    liczba=1993
    dzisiaj=date.today()
    now = datetime.now()
    data = dzisiaj.strftime("%d/%m/%Y")
    godzina = now.strftime("%H:%M:%S")
    print(godzina)
    # return HttpResponse('Witaj na stronie Agaty')
    print('ktoś ogląda moją stronę')
    return render(request, 'szablonAgaty.html', {'dzisiaj':data, 'liczba':liczba, 'godzina':godzina, })