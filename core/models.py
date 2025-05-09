from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username



class Destination(models.Model):
    titre = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    prix_par_personne = models.DecimalField(max_digits=8, decimal_places=2)
    duree = models.PositiveIntegerField(help_text="Durée du séjour en jours")
    date_debut = models.DateField()
    date_fin = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titre} – {self.lieu}"

class Reservation(models.Model):
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('CONFIRMEE', 'Confirmée'),
        ('ANNULEE', 'Annulée'),
    ]

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    nb_personnes = models.PositiveIntegerField()
    date_reservation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='EN_ATTENTE')

    def __str__(self):
        return f"{self.utilisateur.username} → {self.destination.titre}"



class Paiement(models.Model):
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('SUCCES', 'Succès'),
        ('ECHEC', 'Échec'),
    ]

    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    stripe_payment_id = models.CharField(max_length=255)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='EN_ATTENTE')
    date_paiement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reservation} – {self.statut}"



class Avis(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    commentaire = models.TextField()
    note = models.IntegerField(choices=[(i, f"{i}/5") for i in range(1, 6)])
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Avis {self.note}/5 – {self.reservation.destination.titre}"
