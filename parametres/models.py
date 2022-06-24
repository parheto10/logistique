from django.db import models

ETAT = (
    ('en_cours', 'EN COURS'),
    ('suspendu', 'SUSPENDU'),
    ('traite', 'TRAITE'),
)

POSTE = (
    ('AIDE', 'AIDE'),
    ('PEPINIERISTE', 'PEPINIERISTE'),
    ('SUPERVISEUR', 'SUPERVISEUR'),
    ('TECHNICIEN', 'TECHNICIEN AGRICOLE'),
    ('AUTRE', 'AUTRE'),
)

class Responsable(models.Model):
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255, blank=True, null=True)
    contact1 = models.CharField(max_length=255)
    contact2 = models.CharField(max_length=255, blank=True, null=True)
    email_pro = models.EmailField()

    def __str__(self):
        Nom = self.nom + self.prenoms
        return "%s - (%s)" %(Nom, self.poste)

    class Meta:
        verbose_name_plural = "RESPONSABLES PROJETS"
        verbose_name = "responsable projet"
        ordering = ["nom"]

    def save(self, force_insert=False, force_update=False):
        self.nom = self.nom.upper()
        self.poste = self.poste.upper()
        self.prenoms = self.prenoms.upper()
        super(Responsable, self).save(force_insert, force_update)

class Projet(models.Model):
    sigle = models.CharField(max_length=255)
    titre = models.CharField(max_length=500)
    chef = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    debut = models.DateField()
    fin = models.DateField()
    etat = models.CharField(max_length=50, choices=ETAT)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return "%s" %(self.sigle)

    class Meta:
        verbose_name_plural = "PROJETS"
        verbose_name = "projet"
        ordering = ["sigle"]

    def save(self, force_insert=False, force_update=False):
        self.sigle = self.sigle.upper()
        self.titre = self.titre.upper()
        super(Projet, self).save(force_insert, force_update)

class Technicien(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255, blank=True, null=True)
    localite = models.CharField(max_length=255)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    contact1 = models.CharField(max_length=255)
    contact2 = models.CharField(max_length=255, blank=True, null=True)
    poste = models.CharField(max_length=255, verbose_name='POSTE OCCUPE', choices=POSTE)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return "%s - %s" %(self.nom, self.prenoms)

    class Meta:
        verbose_name_plural = "TECHNICIENS"
        verbose_name = "technicien"
        ordering = ["nom"]

    def save(self, force_insert=False, force_update=False):
        self.nom = self.nom.upper()
        self.prenoms = self.prenoms.upper()
        self.localite = self.localite.upper()
        super(Technicien, self).save(force_insert, force_update)


# Create your models here.
