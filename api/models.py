from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coordinate(models.Model):
    longitude = models.FloatField()
    lagitude = models.FloatField()
    
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Coordinate."""

        verbose_name = " Coordonnées"
        verbose_name_plural = " Coordonnées "


class Salon(models.Model):

    """Model definition for Salon."""
    nom = models.CharField(max_length=100)
    description = models.TextField()
    coordonnees = models.ForeignKey(Coordinate, on_delete=models.CASCADE, related_name="coordonnees_salon")

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Salon."""

        verbose_name = "Nos salons"
        verbose_name_plural = "Nos salons"

    def __str__(self):
        """Unicode representation of Salon."""
        return self.nom

class Service(models.Model):
    """Model definition for Tag."""
    nom = models.CharField(max_length=50)
    description = models.TextField()
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="Services_salons")

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Nos Services'
        verbose_name_plural = 'Nos Services'

    def __str__(self):
        """Unicode representation of Services."""
        return self.nom



class Photo(models.Model):
    """Model definition for Photo."""
    image = models.ImageField(upload_to='images/salon/photo/')
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="photo_salon")

    status = models.BooleanField(default=False,null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Photo."""

        verbose_name = ' Nos Photos'
        verbose_name_plural = 'Nos Photos'

    
    

