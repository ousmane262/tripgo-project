from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Destination, Reservation, Paiement, Avis

from django.shortcuts import get_object_or_404


User = get_user_model()

# 🔹 Page d'accueil publique
def home(request):
    return render(request, 'home.html')

# 🔐 Connexion
def connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('userprofile')
        else:
            messages.error(request, "Email ou mot de passe incorrect.")
    return render(request, 'connexion.html')

# 🔐 Inscription
def inscription(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = nom
            user.save()
            login(request, user)
            messages.success(request, "Inscription réussie ! Vous êtes maintenant connecté.")
            return redirect('userprofile')
    return render(request, 'inscription.html')

# 🔓 Déconnexion
def deconnexion(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('connexion')

# 🧭 Tableau de bord utilisateur (profil)
@login_required
def userprofile(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = request.user
        user.first_name = nom
        user.email = email
        user.username = nom  #

        if password:
            user.set_password(password)
            update_session_auth_hash(request, user)  # Rester connecté

        user.save()
        messages.success(request, "Profil mis à jour avec succès.")

    # 🔄 Chargement des données utilisateur
    reservations = Reservation.objects.filter(utilisateur=request.user).select_related('destination')
    paiements = Paiement.objects.filter(reservation__utilisateur=request.user).select_related('reservation')
    avis = Avis.objects.filter(reservation__utilisateur=request.user).select_related('reservation')

    return render(request, 'userprofile.html', {
        'user': request.user,
        'reservations': reservations,
        'paiements': paiements,
        'avis': avis
    })

# 📅 Page dédiée aux réservations (si besoin)
@login_required
def mes_reservations(request):
    reservations = Reservation.objects.filter(utilisateur=request.user).select_related('destination')
    return render(request, 'mes_reservations.html', {'reservations': reservations})


from django.shortcuts import get_object_or_404

@login_required
def reserver_destination(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)

    if request.method == 'POST':
        try:
            nb_personnes = int(request.POST.get('nb_personnes', 1))

            reservation = Reservation.objects.create(
                utilisateur=request.user,
                destination=destination,
                nb_personnes=nb_personnes,
                statut='CONFIRMEE'
            )

            Paiement.objects.create(
                reservation=reservation,
                montant=destination.prix_par_personne * nb_personnes,
                stripe_payment_id="PAIEMENT_FAUX_001",
                statut='SUCCES'
            )

            messages.success(request, "Réservation et paiement simulé enregistrés avec succès.")
            return redirect('userprofile')

        except Exception as e:
            messages.error(request, f"Erreur : {str(e)}")
            return redirect('reserver_destination', destination_id=destination.id)

    return render(request, 'reserver_destination.html', {'destination': destination})

