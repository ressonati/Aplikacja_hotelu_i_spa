from django.contrib import admin
from .models import Pokoj,Dodatkowe_uslugi,Pobyt,Rezerwacja_pokoju,Usluga_spa,Rezerwacja_uslugi_spa


admin.site.register(Pokoj)
admin.site.register(Dodatkowe_uslugi)
admin.site.register(Pobyt)
admin.site.register(Rezerwacja_pokoju)
admin.site.register(Usluga_spa)
admin.site.register(Rezerwacja_uslugi_spa)

