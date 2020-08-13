from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(
        max_length=255, null=True, blank=True)
    country = models.CharField(
        max_length=50, null=True, blank=True)
    province = models.CharField(
        max_length=50,null=True, blank=True)
    city = models.CharField(
        max_length=50, null=True, blank=True)
    zip_code = models.CharField(
        max_length=10,  null=True, blank=True)
        
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("address:address-detail", kwargs={"pk": self.pk})
