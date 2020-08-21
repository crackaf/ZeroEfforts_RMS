from django.db import models
from address.models import Address
# Create your models here.


class Customer(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False)
    phone = models.CharField(
        max_length=50, null=False, blank=True)
    email = models.EmailField(
        default='zeroefforts.dev@gmail.com', null=False, blank=False)

    address=models.ForeignKey(
        Address, on_delete=models.DO_NOTHING, null=True, blank=True)
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customer:customer-detail", kwargs={"pk": self.pk})
