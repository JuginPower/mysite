from django.db import models
import re


class MathService():

    def to_float(self, str_number: str, absolut=True):

        result = None

        try:
            if len(str_number) > 7:
                result = str_number.replace(".", "_").replace(",", ".")
            
            elif len(str_number) <= 7:
                result = str_number.replace(",", ".")

            if absolut:
                result = abs(float(result))
            elif not absolut:
                result = float(result)
        
        except ValueError as err:
            return str(err)
        
        return result


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Keyword(models.Model):

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 related_name="keywords")
    
    def __str__(self) -> str:
        return self.name


class Activity(models.Model):

    KIND_NAMES = {"reg": "Regular", "irr": "Irregular"}

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, 
                                 blank=True, related_name="activities")
    
    date = models.DateField()
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=3, choices=KIND_NAMES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name
