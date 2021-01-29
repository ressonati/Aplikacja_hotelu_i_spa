from django.db import models
import datetime
from django.contrib.auth.models import User


class Pokoj(models.Model):
    Standard_lista = (('podstawowy','podstawowy'),
                      ('wyzszy','wyzszy'),
                     )
    Rodzaj_lista = (
        ('jednoosobowy','jednoosobowy'),
        ('dwuosobowy','dwuosobowy'),
        ('trzyosobowy','trzyosobowy'),
    )
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    nazwa_pokoju = models.CharField(max_length=20)
    opis_pokoju = models.CharField(max_length=255, blank=True)
    standard = models.CharField(max_length=20, choices=Standard_lista,default='podstawowy')
    rodzaj = models.CharField(max_length=20,choices=Rodzaj_lista,default='jednoosobowy')
    img = models.CharField(max_length=50, blank=True)
    # czy_dostawka = models.BooleanField(default=False,verbose_name = ('Dostawka dla dziecka'))

    def __str__(self):
        return self.nazwa_pokoju

    class Meta:
        verbose_name = "Pokoj"
        verbose_name_plural = "Pokoje"


class Dodatkowe_uslugi(models.Model):
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    nazwa_dodatkowej_uslugi = models.CharField(max_length=25)
    opis_uslugi = models.CharField(max_length=255, blank=True)


    class Meta:
        verbose_name = "Dodatkowa usluga"
        verbose_name_plural = "Dodatkowe uslugi"

    def __str__(self):
        return self.nazwa_dodatkowej_uslugi


class Pobyt(models.Model):
    data_zakwaterowania = models.DateField("Data_zakwaterowania")
    data_wykwaterowania = models.DateField(("Data_wykwaterowania"), blank=True)

    # Relacja 1 do 1 z rezerwacja pokoju, jak to zrobic?
    # rezerwacja_pokoju = models.ForeignKey(Rezerwacja_pokoju, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.data_zakwaterowania

    class Meta:
        verbose_name = "Pobyt"
        verbose_name_plural = "Pobyty"


class Rezerwacja_pokoju(models.Model):
    status_1 = 'Zatwierdzony'
    status_2 = 'Niezatwierdzony'
    cena_calkowita = models.DecimalField(max_digits=20, decimal_places=2)
    data_do = models.DateField(blank=True)
    data_od = models.DateField(blank=True)
    ilosc_dni = models.IntegerField(blank=True)
    status = ((status_1, 'Zatwierdzony'), (status_2, 'Niezatwierdzony'))

    pokoj = models.ForeignKey(Pokoj, on_delete=models.CASCADE, null=True)
    #?? one to one field
    # pobyt = models.OneToOneField(Pobyt, on_delete=models.CASCADE, null=True)
    dodatkowe_uslugi = models.ForeignKey(Dodatkowe_uslugi, on_delete=models.CASCADE, null=True)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Rezerwacja pokoju"
        verbose_name_plural = "Rezerwacje pokojow"


class Usluga_spa(models.Model):
    cena_jednostkowa = models.DecimalField(decimal_places=2, max_digits=5)
    nazwa_uslugi = models.CharField(max_length=50)
    opis_uslugi = models.CharField(max_length=255, blank=True)
    img = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "Usluga spa"
        verbose_name_plural = "Uslugi spa"

    def __str__(self):
        return self.nazwa_uslugi


class Rezerwacja_uslugi_spa(models.Model):
    data_rezerwacji = models.DateField()
    godzina_rezerwacji = models.TimeField()
    ilosc_osob = models.IntegerField()
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    usluga_spa = models.ForeignKey(Usluga_spa, on_delete=models.CASCADE, null=True)

    def __str__(self):
        # Czy dziala Usluga_spa.nazwa_uslugi
        return self.usluga_spa.nazwa_uslugi

    class Meta:
        verbose_name = "Rezerwacja uslugi spa"
        verbose_name_plural = "Rezerwacje uslug spa"