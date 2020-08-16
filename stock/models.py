from django.db import models
from store.models import Store
from inventory.models import Inventory
# Create your models here.


class Stock(models.Model):
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE)
    inventory = models.ForeignKey(
        Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        null=False, blank=False, default=0)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
        unique_together=['store', 'inventory']

    def __str__(self):
        return (self.store.name+"\t"+self.inventory.name)

    def get_absolute_url(self):
        return reverse("stock_detail", kwargs={"pk": self.pk})
