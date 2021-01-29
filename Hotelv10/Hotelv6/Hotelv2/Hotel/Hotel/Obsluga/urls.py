from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('przegladaj-dostepne-pokoje', views.pokoje, name='pokoje'),
    path('przegladaj-uslugi-spa', views.spa, name='spa'),
    path('przegladaj-pokoje', views.infopokoje, name='infopokoje'),
    path('przegladaj-spa', views.infospa, name='infospa'),
    # path('onas', views.onas, name='onas'),
    path('zarejestruj', views.rejestruj, name='rejestruj'),
    path('zaloguj', views.zaloguj, name='zaloguj'),
    path('wyloguj', views.wyloguj, name='wyloguj'),
    path('zarzadzaj-pokoje', views.zarzadzaj_pokoje, name='zarzadzaj pokojami'),
    path('nowa-rezerwacja-pokoju', views.nowa_rezerwacja_pokoju, name="nowa rezerwacja pokoju"),
    path('edycja-rezerwacji-pokoju/<int:pk>', views.edytuj_rezerwacje_pokoju, name='edycja rezerwacji pokoju'),
    path('usun-rezerwacje-pokoju/<int:pk>', views.usun_rezerwacje_pokoju, name='usun rezerwacje pokoju'),
    path('zarzadzaj-spa', views.zarzadzaj_spa, name='zarzadzaj spa'),
    path('nowa-rezerwacja-spa', views.nowa_rezerwacja_spa, name="nowa rezerwacja spa"),
    path('edycja-rezerwacji-spa/<int:pk>', views.edytuj_rezerwacje_spa, name='edycja rezerwacji spa'),
    path('usun-rezerwacje-spa/<int:pk>', views.usun_rezerwacje_spa, name='usun rezerwacje spa'),
    path('zarzadzaj-uzytkownikami', views.zarzadzaj_uzytkownikami, name="zarzadzaj uzytkownikami"),
    path('nowy-uzytkownik', views.nowy_uzytkownik, name="nowy-uzytkownik"),
    path('edycja-uzytkownika/<int:pk>', views.edycja_uzytkownika, name='edycja uzytkownika'),
    path('usun-uzytkownika/<int:pk>', views.usun_uzytkownika, name='usun uzytkownika'),
    path('rezerwuj-pokoj/<int:pk>', views.rezerwuj_pokoj, name='rezerwuj pokoj'),
    path('rezerwuj-spa/<int:pk>', views.rezerwuj_spa, name='rezerwuj spa'),
    path('pomyslna-rezerwacja', views.pomyslna_rezerwacja, name='Pomyslna rezerwacja'),
]
