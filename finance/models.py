from django.db import models


class Kategorie(models.Model):

    name = models.CharField(max_length=50)


class Keyword(models.Model):

    name = models.CharField(max_length=50)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE)


class Bilanz(models.Model):

    datum = models.DateField()
    einnahmen = models.DecimalField(max_digits=10, decimal_places=2)
    ausgaben = models.DecimalField(max_digits=10, decimal_places=2)
