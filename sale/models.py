from django.db import models
from customer.models import Customer
from inventory.models import Inventory
# Create your models here.


class Sale(models.Model):

    customer = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING)

    # Making choices
    COMPLETED = 'CO'
    REJECTED = 'RE'
    PENDING = 'PE'
    PROCESSING = 'PR'
    ORDER_STATUS_CHOICES = [
        (COMPLETED, 'Completed'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
    ]
    order_status = models.CharField(
        max_length=50, choices=ORDER_STATUS_CHOICES, default=PROCESSING)

    order_date = models.DateTimeField(auto_now=True)
    # required date
    # shipped date
    # store = models.ForeignKey(
    #     Store, on_delete=models.CASCADE)
    # staff = models.ForeignKey(
    #     Staff, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sale_detail", kwargs={"pk": self.pk})


class SaleDetail(models.Model):
    sale = models.ForeignKey(
        Sale, on_delete=models.CASCADE)
    inventory = models.ForeignKey(
        Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        null=False, blank=False)
    price = models.FloatField(
        null=False, blank=False)
    discount = models.FloatField(
        null=False, blank=False, default=0)

    class Meta:
        verbose_name = _("OrderDetail")
        verbose_name_plural = _("OrderDetail")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("OrderDetail_detail", kwargs={"pk": self.pk})
