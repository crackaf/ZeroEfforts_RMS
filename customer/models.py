from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False)
    phone = models.CharField(
        max_length=50, null=False, blank=True)
    email = models.EmailField(
        default='zeroefforts.dev@gmail.com', null=False, blank=False)
    
    # address=models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=true)

    def __str__(self):
        return self.name
