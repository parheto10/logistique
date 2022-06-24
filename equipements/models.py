from django.db import models

from parametres.models import Projet, Responsable, Technicien

# Create your models here.

ACCESSOIRES = (
    ('PILE', 'PILE'),
    ('CABLE','CABLE')
)

MARQUE=(
    ('GARMIN', 'GARMIN'),
    ('AUTRE', 'AUTRE')
)

MARQUE_PC = (
    ('ASUS', 'ASUS'),
    ('DELL', 'DELL'),
    ('HP', 'HP'),
)

class Accessoire(models.Model):
    libelle = models.CharField(max_length=255)

    def __str__(self):
        return "%s" %(self.libelle)

class Ordinateur(models.Model):
    code = models.CharField(max_length=225)
    numero_serie = models.CharField(max_length=225)
    marque = models.CharField(max_length=225, choices=MARQUE_PC)
    model = models.CharField(max_length=225, blank=True, null=True)
    utilisateur = models.CharField(max_length=225)
    date_achat = models.DateField(null=True, blank=True)
    prix_achat = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "ORDNATEURS"
        verbose_name = "ordinateurs"
        ordering = ["code"]

    def save(self, force_insert=False, force_update=False):
        self.code = self.code.upper()
        self.numero_serie = self.numero_serie.upper()
        self.utilisateur = self.utilisateur.upper()
        if self.model:
            self.model = self.model.upper()
        super(Ordinateur, self).save(force_insert, force_update)


class Imprimante(models.Model):
    code = models.CharField(max_length=225)
    numero_serie = models.CharField(max_length=225)
    marque = models.CharField(max_length=225, choices=MARQUE_PC)
    model = models.CharField(max_length=225, blank=True, null=True)
    utilisateur = models.CharField(max_length=225)
    date_achat = models.DateField(null=True, blank=True)
    prix_achat = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "IMPRIMANTES"
        verbose_name = "imprimantes"
        ordering = ["code"]

    def save(self, force_insert=False, force_update=False):
        self.code = self.code.upper()
        self.numero_serie = self.numero_serie.upper()
        self.utilisateur = self.utilisateur.upper()
        if self.model:
            self.model = self.model.upper()
        super(Imprimante, self).save(force_insert, force_update)


class Gps(models.Model):
    code = models.CharField(max_length=225)
    marque = models.CharField(max_length=225, choices=MARQUE, default="GARMIN")
    model = models.CharField(max_length=225, blank=True, null=True)
    prix_achat = models.PositiveIntegerField(default=0)
    date_achat = models.DateField(null=True, blank=True)


    def __str__(self):
        return "%s - %s" %(self.code, self.marque)

    class Meta:
        verbose_name_plural = "GPS"
        verbose_name = "gps"
        ordering = ["code"]

    def save(self, force_insert=False, force_update=False):
        self.code = self.code.upper()
        if self.model:
            self.model = self.model.upper()
        super(Gps, self).save(force_insert, force_update)



class Sortiequipement(models.Model):
    technicien = models.ForeignKey(Technicien,on_delete=models.CASCADE, blank=True, null=True)
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE, blank=True, null=True)
    gps = models.ForeignKey(Gps,on_delete=models.CASCADE, blank=True, null=True)
    date_sortie = models.DateField(null=True, blank=True)
    accessoires = models.ManyToManyField(Accessoire)

    def __str__(self):
        return "%s - %s" %(self.technicien,self.accessoires)

    class Meta:
        verbose_name_plural = "SORTIE EQUIPEMENTS"
        verbose_name = "sortie equipement"
        ordering = ["-date_sortie"]
