from django.db import models
from django.conf import settings

# Create your models here.


class Inventory(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False)
    price = models.FloatField(
        null=False, blank=False)
    # brand = models.ForeignKey(
    #     Brand, on_delete=models.CASCADE, null=True, blank=True)
    # category = models.ManyToManyField(
    #     Category, on_delete=models.CASCADE,  null=True, blank=True)
    description = models.TextField(
        null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=False)
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='%(class)s_product_created')
    updatedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='%(class)s_product_updated')

    def __str__(self):
        return self.name
