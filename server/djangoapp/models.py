from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dealer_id = models.IntegerField()
    SEDAN="Sedan"
    SUV="SUV"
    WAGON="WAGON"
    TYPE_CHOICES = (
        (SEDAN,"Sedan"),
        (SUV,"SUV"),
        (WAGON,"Wagon"),
    )
    model_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    year = models.DateField()
    
    def __str__(self):
        return f"{self.make} {self.name} ({self.year})"
