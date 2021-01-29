from django import forms
from Obsluga.models import Pokoj, Dodatkowe_uslugi, Pobyt, Rezerwacja_pokoju, Usluga_spa, Rezerwacja_uslugi_spa
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class Rezerwacja_pokoi_Form(forms.ModelForm):
    class Meta:
        model = Rezerwacja_pokoju
        # fileds = ['cena_calkowita','data_do','data_od','status']
        # fields = ['cena_calkowita','data_od','data_do','ilosc_dni', 'pokoj', 'dodatkowe_uslugi','uzytkownik','pobyt']
        fields = '__all__'
        widgets = {
            'data_od' : forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
            'data_do' : forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
            'data_zakwaterowania' : forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
            'data_wykwaterowania' : forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
        }

class Rezerwacja_uslug_spa_Form(forms.ModelForm):
    class Meta:
        model = Rezerwacja_uslugi_spa
        # fileds = ['cena_calkowita','data_do','data_od','status']
        fields = ['data_rezerwacji','godzina_rezerwacji','ilosc_osob','uzytkownik','usluga_spa']
        # fields = '__all__'
        widgets = {
            'data_rezerwacji' : forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
            'godzina_rezerwacji' : forms.TimeInput(attrs={'type' : 'time'})
        }

class Users_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        # fields = '__all__'


class Rezerwacja_pokoju_uzytkownik_Form(forms.ModelForm):
    class Meta:
        model = Rezerwacja_pokoju
        # fileds = ['cena_calkowita','data_do','data_od','status']
        fields = ['data_od','data_do', 'dodatkowe_uslugi', 'ilosc_dni']
        # fields = '__all__'
        widgets = {
            'data_od' : forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
            'data_do' : forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
            # 'data_zakwaterowania' : forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
            # 'data_wykwaterowania' : forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
        }



class Rezerwacja_uslug_spa_uzytkownik_Form(forms.ModelForm):
    class Meta:
        model = Rezerwacja_uslugi_spa
        # fileds = ['cena_calkowita','data_do','data_od','status']
        #'uzytkownik','usluga_spa'!!
        fields = ['data_rezerwacji','godzina_rezerwacji','ilosc_osob']
        # fields = '__all__'
        widgets = {
            'data_rezerwacji' : forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
            'godzina_rezerwacji' : forms.TimeInput(attrs={'type' : 'time'})
        }