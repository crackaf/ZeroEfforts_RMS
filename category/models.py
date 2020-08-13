from django.db import models
from django.shortcuts import reverse
from simple_history.models import HistoricalRecords

# Create your models here.


class Category(models.Model):

    name = models.CharField(
        max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    history= HistoricalRecords()


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category:category-detail", kwargs={"pk": self.pk})
