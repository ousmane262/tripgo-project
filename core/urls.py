from django.urls import path
from . import views

urlpatterns = [

    # 🔓 Authentification
    path('', views.home, name='home'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),

    # 👤 Espace utilisateur (tableau de bord)
    path('profil/', views.userprofile, name='userprofile'),

    # 🔁 Vues AJAX dynamiques (dashboard)
    path('profil/reservations/', views.mes_reservations, name='mes_reservations'),
    path('reserver/<int:destination_id>/', views.reserver_destination, name='reserver_destination'),


]
