from django.db import models

class Demande(models.Model):
    # Informations personnelles
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    parking_address = models.BooleanField(default=False)  # Parking personnel

    # Informations supplémentaires
    birth_date = models.DateField(null=True, blank=True)

    # Informations du véhicule
    vehicle_brand = models.CharField(max_length=100, null=True, blank=True)
    engine_capacity = models.IntegerField(null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    registration_number = models.CharField(max_length=50, null=True, blank=True)
    first_registration_date = models.DateField(null=True, blank=True)
    acquisition_date = models.DateField(null=True, blank=True)

    # Informations sur les permis
    permis_a1 = models.DateField(null=True, blank=True)
    permis_a2 = models.DateField(null=True, blank=True)
    permis_a = models.DateField(null=True, blank=True)
    permis_b = models.DateField(null=True, blank=True)

    annulation_a1 = models.BooleanField(default=False)
    annulation_a2 = models.BooleanField(default=False)
    annulation_a = models.BooleanField(default=False)
    annulation_b = models.BooleanField(default=False)

    # Champs relatifs à l'option de moto et l'annulation
    selected_option = models.CharField(max_length=50, null=True, blank=True)
    moto_option = models.CharField(max_length=50, null=True, blank=True)
    annulation = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    project_purchase = models.BooleanField(default=False)

    # Informations complémentaires (page de confirmation)
    informations_complementaires = models.TextField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
