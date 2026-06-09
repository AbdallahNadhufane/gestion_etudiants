from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

