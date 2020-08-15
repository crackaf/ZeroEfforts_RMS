from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False)
    description = models.TextField(
        null=True, blank=True)
    
    #address
    

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store_detail", kwargs={"pk": self.pk})
