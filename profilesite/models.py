from django.db import models
from django.contrib.auth.models import User


class Bouncer(models.Model):

    APPLICATIONS = [("pr", "profilesite"), ("bl", "blogs")]
    purpose = models.CharField(max_length=2, choices=APPLICATIONS, default="pr")
    permission = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Bouncer: {self.purpose}"
