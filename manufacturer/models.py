from django.db import models
from django.urls import reverse
# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False)
    detail = models.TextField(
        null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manufacturer:manufacturer-detail", args=[str(self.id)])
