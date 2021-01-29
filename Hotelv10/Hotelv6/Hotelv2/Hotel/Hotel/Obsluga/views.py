from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from Obsluga.models import Pokoj, Dodatkowe_uslugi, Rezerwacja_pokoju, Usluga_spa, Rezerwacja_uslugi_spa
from .forms import Rezerwacja_pokoi_Form, Rezerwacja_uslug_spa_Form, Users_Form, Rezerwacja_pokoju_uzytkownik_Form, \
    Rezerwacja_uslug_spa_uzytkownik_Form


# Create your views here.


def index(request):
    return render(request, 'index.html')


#
# def onas(request):
#     return render(request, 'onas.html')
#
#

def pokoje(request):
    return render(request, 'przegladaj-dostepne-pokoje.html')


def spa(request):
    return render(request, 'przegladaj-uslugi-spa.html')


def infopokoje(request):
    pokoje = Pokoj.objects.all()
    dane = {'pokoje': pokoje}
    return render(request, 'przegladaj-pokoje.html', dane)


def infospa(request):
    spa = Usluga_spa.objects.all()
    dane = {'spa': spa}
    return render(request, 'przegladaj-spa.html', dane)


def zarzadzaj_pokoje(request):
    pokoje_zarzadzaj = Rezerwacja_pokoju.objects.all()
    dane = {'pokoje_zarzadzaj': pokoje_zarzadzaj}
    return render(request, 'zarzadzaj-pokoje.html', dane)


def zaloguj(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Niepoprawne dane')
            return redirect('zaloguj')
    else:
        return render(request, 'zaloguj.html')


def rejestruj(request):
    if request.method == 'POST':
        email = request.POST['email']
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Istenieje już konto o tym adresie email')
                return redirect('zarejestruj')
            else:
                user = User.objects.create_user(username=email, first_name=imie, last_name=nazwisko, email=email,
                                                password=password1)
                user.save()
                return redirect('zaloguj')
        else:
            messages.info(request, 'Podane hasła nie są identyczne')
            return redirect('zarejestruj')
    else:
        return render(request, 'zarejestruj.html')


def wyloguj(request):
    auth.logout(request)
    return redirect('/')


def nowa_rezerwacja_pokoju(request):
    szablon = 'nowa-rezerwacja-pokoju.html'
    form = Rezerwacja_pokoi_Form(request.POST or None)

    try:
        if form.is_valid():
            messages.success(request, 'Zapisano rekord do tabeli Rezerwacji pokojów')
            form.save()
            return HttpResponseRedirect('/zarzadzaj-pokoje')

    except Exception as e:
        form = Rezerwacja_pokoi_Form()
        messages.warning(request, 'Wystąpił błąd podczas zapisywania rekordu do tabeli,\n Błąd:{}'.format(e))

    dane = {'form': form}

    return render(request, szablon, dane)


def edytuj_rezerwacje_pokoju(request, pk):
    szablon = 'edycja-rezerwacji-pokoju.html'
    rezerwacja = get_object_or_404(Rezerwacja_pokoju, pk=pk)

    if request.method == "POST":
        form = Rezerwacja_pokoi_Form(request.POST, instance=rezerwacja)

        try:
            if form.is_valid():
                messages.success(request, 'Pomyslnie zapisano edytowany rekord')
                form.save()
                return HttpResponseRedirect('/zarzadzaj-pokoje')
        except Exception as e:
            messages.warning(request, 'Wystapil blad podczas zapisywania edytowanego rekordu \n Błąd:{}', format(e))
    else:
        form = Rezerwacja_pokoi_Form(instance=rezerwacja)

    dane = {'form': form,
            'rezerwacja': rezerwacja}
    return render(request, szablon, dane)


def usun_rezerwacje_pokoju(request, pk):
    szablon = 'edycja-rezerwacji-pokoju.html'

    rezerwacja = get_object_or_404(Rezerwacja_pokoju, pk=pk)

    form = Rezerwacja_pokoi_Form(instance=rezerwacja)
    form = Rezerwacja_pokoi_Form(request.POST, instance=rezerwacja)
    messages.success(request, "Pomyslnie usunieto rekord z tabeli")
    rezerwacja.delete()
    return HttpResponseRedirect('/zarzadzaj-pokoje')
    dane = {'form': form,
            'rezerwacja': rezerwacja, }
    return render(request, szablon, dane)


def zarzadzaj_spa(request):
    spa_zarzadzaj = Rezerwacja_uslugi_spa.objects.all()
    dane = {'spa_zarzadzaj': spa_zarzadzaj}
    return render(request, 'zarzadzaj-spa.html', dane)


def nowa_rezerwacja_spa(request):
    szablon = 'nowa-rezerwacja-spa.html'
    form = Rezerwacja_uslug_spa_Form(request.POST or None)

    try:
        if form.is_valid():
            messages.success(request, 'Pomyslnie zapisano nowy rekord do tabeli')
            form.save()
            return HttpResponseRedirect('/zarzadzaj-spa')

    except Exception as e:
        form = Rezerwacja_pokoi_Form()
        messages.warning(request, 'Wystąpił błąd podczas zapisywania rekordu do tabeli,\n Błąd:{}'.format(e))

    dane = {'form': form}

    return render(request, szablon, dane)


def edytuj_rezerwacje_spa(request, pk):
    szablon = 'edycja-rezerwacji-spa.html'
    rezerwacja = get_object_or_404(Rezerwacja_uslugi_spa, pk=pk)

    if request.method == "POST":
        form = Rezerwacja_uslug_spa_Form(request.POST, instance=rezerwacja)

        try:
            if form.is_valid():
                messages.success(request, 'Pomyslnie zapisano edytowany rekord')
                form.save()
                return HttpResponseRedirect('/zarzadzaj-spa')
        except Exception as e:
            messages.warning(request, 'Wystapil blad podczas zapisywania edytowanego rekordu \n Błąd:{}', format(e))
    else:
        form = Rezerwacja_uslug_spa_Form(instance=rezerwacja)

    dane = {'form': form,
            'rezerwacja': rezerwacja}
    return render(request, szablon, dane)


def usun_rezerwacje_spa(request, pk):
    szablon = 'edycja-rezerwacji-spa.html'

    rezerwacja = get_object_or_404(Rezerwacja_uslugi_spa, pk=pk)

    form = Rezerwacja_uslug_spa_Form(instance=rezerwacja)
    form = Rezerwacja_uslug_spa_Form(request.POST, instance=rezerwacja)
    messages.success(request, "Pomyslnie usunieto rekord z tabeli")
    rezerwacja.delete()
    return HttpResponseRedirect('/zarzadzaj-spa')
    dane = {'form': form,
            'rezerwacja': rezerwacja, }
    return render(request, szablon, dane)


def zarzadzaj_uzytkownikami(request):
    uzytkownicy_zarzadzaj = User.objects.filter(is_staff=False)
    dane = {'uzytkownicy_zarzadzaj': uzytkownicy_zarzadzaj}
    return render(request, 'zarzadzaj-uzytkownikami.html', dane)


# def nowy_uzytkownik(request):
#     szablon = 'nowy-uzytkownik.html'
#     form = Users_Form(request.POST or None)
#
#     try:
#         if form.is_valid():
#             messages.success(request, 'Pomyslnie zapisano nowy rekord do tabeli')
#             new_user = User.objects.create_user(**form.cleaned_data)
#             # form.save()
#             return HttpResponseRedirect('/zarzadzaj-uzytkownikami')
#
#     except Exception as e:
#         form = Users_Form()
#         messages.warning(request, 'Wystąpił błąd podczas zapisywania rekordu do tabeli,\n Błąd:{}'.format(e))
#     else:
#         form = Users_Form()
#
#     dane = { 'form'  : form}
#
#     return render(request, szablon, dane)
#

def nowy_uzytkownik(request):
    if request.method == 'POST':
        email = request.POST['email']
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        password1 = request.POST['password1']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Istenieje już konto o tym adresie email')
            return redirect('nowy-uzytkownik')
        else:
            user = User.objects.create_user(username=email, first_name=imie, last_name=nazwisko, email=email,
                                            password=password1)
            user.save()
            return HttpResponseRedirect('/zarzadzaj-uzytkownikami')

    else:
        return render(request, 'nowy-uzytkownik.html')


def edycja_uzytkownika(request, pk):
    szablon = 'edycja-uzytkownika.html'
    rezerwacja = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        form = Users_Form(request.POST, instance=rezerwacja)

        try:
            if form.is_valid():
                messages.success(request, 'Pomyslnie zapisano edytowany rekord')
                form.save()
                return HttpResponseRedirect('/zarzadzaj-uzytkownikami')
        except Exception as e:
            messages.warning(request, 'Wystapil blad podczas zapisywania edytowanego rekordu \n Błąd:{}'.format(e))
    else:
        form = Users_Form(instance=rezerwacja)

    dane = {'form': form,
            'rezerwacja': rezerwacja}
    return render(request, szablon, dane)


def usun_uzytkownika(request, pk):
    szablon = 'edycja-uzytkownika.html'

    rezerwacja = get_object_or_404(User, pk=pk)

    form = Users_Form(instance=rezerwacja)
    form = Users_Form(request.POST, instance=rezerwacja)
    messages.success(request, "Pomyslnie usunieto rekord z tabeli")
    rezerwacja.delete()
    return HttpResponseRedirect('/zarzadzaj-uzytkownikami')
    dane = {'form': form,
            'rezerwacja': rezerwacja, }
    return render(request, szablon, dane)


def rezerwuj_pokoj(request, pk):
    pokoj = Pokoj.objects.filter(pk=pk)
    form = Rezerwacja_pokoju_uzytkownik_Form(request.POST or None)
    uzytkownik = request.user

    if form.is_valid():
        aa = request.POST.dict()
        data_od = aa.get('data_od')
        data_do = aa.get('data_do')

        ilosc_dni = aa.get('ilosc_dni')

        dodatkowe_uslugi = aa.get('dodatkowe_uslugi')
        dodatkowe_uslugi_obiekt = get_object_or_404(Dodatkowe_uslugi, pk=dodatkowe_uslugi)

        pokoj_obiekt = get_object_or_404(Pokoj, pk=pk)

        cena = int(pokoj_obiekt.cena) * int(ilosc_dni)
        obiekt = Rezerwacja_pokoju(data_od=data_od, data_do=data_do, uzytkownik=uzytkownik, cena_calkowita=cena,
                                   ilosc_dni=ilosc_dni, dodatkowe_uslugi=dodatkowe_uslugi_obiekt, pokoj=pokoj_obiekt)
        obiekt.save()
        return HttpResponseRedirect('/pomyslna-rezerwacja')
    # form = Rezerwacja_poko

    dane = {'pokoj': pokoj,
            'form': form}

    return render(request, 'rezerwuj-pokoj.html', dane)


def rezerwuj_spa(request, pk):
    spa = Usluga_spa.objects.filter(pk=pk)
    form = Rezerwacja_uslug_spa_uzytkownik_Form(request.POST or None)
    uzytkownik = request.user

    if form.is_valid():
        aa = request.POST.dict()
        data_rezerwacji = aa.get('data_rezerwacji')
        godzina_rezerwacji = aa.get('godzina_rezerwacji')
        ilosc_osob = aa.get('ilosc_osob')

        usluga_spa_obiekt = get_object_or_404(Usluga_spa, pk=pk)
        obiekt = Rezerwacja_uslugi_spa(data_rezerwacji=data_rezerwacji, godzina_rezerwacji=godzina_rezerwacji,
                                       ilosc_osob=ilosc_osob, uzytkownik=uzytkownik, usluga_spa=usluga_spa_obiekt)
        obiekt.save()
        return HttpResponseRedirect('/pomyslna-rezerwacja')

    dane = {'spa': spa,
            'form': form}

    return render(request, 'rezerwuj-spa.html', dane)


def pomyslna_rezerwacja(request):
    return render(request, 'pomyslna-rezerwacja.html')
