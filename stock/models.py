from django.db import models

# Create your models here.


class Stock(models.Model):
    store = models.ForeignKey(
        Store, on_delete=models.SET_NULL)
    inventory = models.ForeignKey(
        Inventory, on_delete=models.SET_NULL)
    quantity=models.IntegerField(
        null=False, blank=False, default=0)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stock_detail", kwargs={"pk": self.pk})
