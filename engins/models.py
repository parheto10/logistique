from django.db import models

from parametres.models import Projet, Responsable, Technicien

TYPE = (
    ('PERSONNEL', 'PERSONNEL'),
    ('CAMION', 'CAMION'),
)

TYPE_MOTO = (
    ('MOTO', 'MOTO'),
    ('TRYCICLE', 'TRYCICLE'),
)

COULEUR = (
    ('BLANCHE', 'BLANCHE'),
    ('GRISE', 'GRISE'),
    ('NOIRE', 'NOIRE'),
)

ACTIVITE = (
    ('CARBURANT', 'CARBURANT'),
    ('VIDANGE', 'VIDANGE'),
    ('REPARATION/ACHAT', 'REPARATION/ACHAT'),
    ('PEAGE', 'PEAGE'),
    ('LAVAGE', 'LAVAGE'),
)

class Chauffeur(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255, blank=True, null=True)
    contact1 = models.CharField(max_length=255)
    contact2 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s - %s" %(self.nom, self.prenoms)

    class Meta:
        verbose_name_plural = "CHAUFFEURS"
        verbose_name = "chauffeur"
        ordering = ["nom"]

    def save(self, force_insert=False, force_update=False):
        self.nom = self.nom.upper()
        self.prenoms = self.prenoms.upper()
        super(Chauffeur, self).save(force_insert, force_update)

class Vehicule(models.Model):
    matricule = models.CharField(max_length=255)
    prix_achat = models.PositiveIntegerField(default=0)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, blank=True, null=True)
    date_achat = models.DateField(blank=True, null=True)
    mise_en_circulation = models.DateField(blank=True, null=True)
    marque = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    couleur = models.CharField(max_length=255, choices=COULEUR)

    def __str__(self):
        return "%s - %s" %(self.matricule, self.model)

    class Meta:
        verbose_name_plural = "VEHICULES"
        verbose_name = "vehicule"
        ordering = ["matricule"]

    def save(self, force_insert=False, force_update=False):
        self.matricule = self.matricule.upper()
        self.marque = self.marque.upper()
        self.model = self.model.upper()
        super(Vehicule, self).save(force_insert, force_update)

class Moto(models.Model):
    type = models.CharField(max_length=255, choices=TYPE_MOTO)
    matricule = models.CharField(max_length=255)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, blank=True, null=True)
    responsable = models.ForeignKey(Technicien, on_delete=models.CASCADE, blank=True, null=True)
    prix_achat = models.PositiveIntegerField(default=0)
    date_achat = models.DateField(blank=True, null=True)
    mise_en_circulation = models.DateField(blank=True, null=True)
    marque = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s - %s" %(self.matricule, self.model)

    class Meta:
        verbose_name_plural = "MOTOS & TRICYCLES"
        verbose_name = "moto et Tricycle"
        ordering = ["matricule"]

    def save(self, force_insert=False, force_update=False):
        self.matricule = self.matricule.upper()
        self.marque = self.marque.upper()
        if self.model:
            self.model = self.model.upper()
        super(Moto, self).save(force_insert, force_update)

class Course(models.Model):
    voiture = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField()
    km_depart = models.PositiveIntegerField(default=0)
    km_arrive = models.PositiveIntegerField(default=0)
    distance = models.PositiveIntegerField(default=0)
    motif = models.CharField(max_length=255)
    chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE)
    responsable = models.CharField(max_length=255)

    def __str__(self):
        return "%s - %s" %(self.motif, self.responsable)

    class Meta:
        verbose_name_plural = "COURSES"
        verbose_name = "course"
        ordering = ["-date"]

class Detail_Course(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    detail = models.CharField(max_length=255, choices=ACTIVITE)
    qte_acheter = models.PositiveIntegerField(default=0)
    prix_unitaire = models.PositiveIntegerField(default=0)
    montant_total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s - %s" %(self.detail, self.montant_total)

    class Meta:
        verbose_name_plural = "DETAILS COURSES"
        verbose_name = "detail course"
        ordering = ["-course_id__date"]


class Mission(models.Model):
    voiture = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    date_depart = models.DateField()
    date_retours = models.DateField(blank=True, null=True)
    nb_jour = models.PositiveIntegerField(default=0)
    ville_depart = models.CharField(max_length=255)
    km_depart = models.PositiveIntegerField(default=0)
    km_arrive = models.PositiveIntegerField(default=0)
    distance = models.PositiveIntegerField(default=0)
    motif = models.CharField(max_length=255)
    frais_location = models.PositiveIntegerField(default=0)
    total_location = models.PositiveIntegerField(default=0)


    def __str__(self):
        return "%s - %s" %(self.motif, self.responsable)

    class Meta:
        verbose_name_plural = "MISSIONS"
        verbose_name = "mission"
        ordering = ["-date_depart"]

class detail_mission(models.Model):
    mission_id = models.ForeignKey(Mission, on_delete=models.CASCADE)
    detail = models.CharField(max_length=255, choices=ACTIVITE)
    qte_acheter = models.PositiveIntegerField(default=0)
    prix_unitaire = models.PositiveIntegerField(default=0)
    montant_total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s - %s" %(self.detail, self.montant_total)

    class Meta:
        verbose_name_plural = "DETAILS MISSIONS"
        verbose_name = "detail mission"
        ordering = ["-mission_id__date_depart"]

class Escale(models.Model):
    localite = models.CharField(max_length=255)
    mission_id = models.ForeignKey(Mission, on_delete=models.CASCADE)
    date_arrivee = models.DateField()
    km_depart = models.PositiveIntegerField(default=0)
    km_arrive = models.PositiveIntegerField(default=0)
    date_depart = models.DateField()

    def __str__(self):
        return "%s - %s" %(self.localite, self.date_arrivee)

    class Meta:
        verbose_name_plural = "ESCALES MISSIONS"
        verbose_name = "escale mission"
        ordering = ["-date_arrivee"]


# Create your models here.
