from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Destination, Reservation, Paiement, Avis

# Personnalisation de l'affichage de l'utilisateur
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_client', 'is_admin', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Rôles personnalisés', {'fields': ('is_client', 'is_admin')}),
    )



@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'lieu', 'prix_par_personne', 'duree', 'active')
    list_filter = ('active', 'lieu')
    search_fields = ('titre', 'lieu')



@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'destination', 'nb_personnes', 'statut', 'date_reservation')
    list_filter = ('statut',)
    search_fields = ('utilisateur__username', 'destination__titre')



@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'montant', 'statut', 'date_paiement')
    list_filter = ('statut',)
    search_fields = ('reservation__utilisateur__username',)


#  Avis
@admin.register(Avis)
class AvisAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'note', 'date')
    search_fields = ('reservation__destination__titre', 'commentaire')
