from django.db import models
from django.contrib.auth.models import User


class Bouncer(models.Model):

    purpose = models.CharField(max_length=50, blank=True, null=True)
    permission = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Bouncer: {self.purpose}"
