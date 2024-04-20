from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator

# seleccion de tipos de vegetales

class Status(models.TextChoices):
    Verduras = 'v', "Verduras de hoja verde"
    Raices = 'r', "Raices"
    Tuberculos = 't', "Tuberculos"
    Temporada = 'd', "Verduras de temporada"

# seleccion de disponibilidad del vegetal

class Actives(models.TextChoices):
    disponible = 'd', "Disponible"
    noDisponible = 'n', "No Disponible"

# datos del vegetal

class Task(models.Model):
    name = models.CharField(
        verbose_name="nombre", 
        max_length=65, 
        unique=True, 
        validators=[
            RegexValidator(
                regex='^[A-Za-z]*$', 
                message='El nombre solo puede contener letras.', 
                code='invalid_name'
            )
        ]
    )
    price = models.PositiveIntegerField(verbose_name="valor por unidad", validators=[MinValueValidator(1)])
    status = models.CharField(verbose_name="Categoria", max_length=1, choices=Status.choices)
    actives = models.CharField(verbose_name="Categoria", max_length=1, choices=Actives.choices)

    def __str__(self):
        return self.name
    
# foranea para guardar en factura

class Facturation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)



