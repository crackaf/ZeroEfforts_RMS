from django.db import models
from django.conf import settings

# Create your models here.


class Brand(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False)
    detail = models.TextField(
        null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False)
    detail = models.TextField(
        null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False)
    price = models.FloatField(
        null=False, blank=False)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,  null=True, blank=True)
    description = models.TextField(
        null=True, blank=True)
    createdDate = models.DateTimeField(auto_now=True)
    updatedDate = models.DateTimeField(auto_now=False)
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='%(class)s_product_created')
    updatedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='%(class)s_product_updated')

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False, unique=True)
    phone = models.CharField(
        max_length=12, null=False, blank=False)
    email = models.EmailField(
        default='zeroefforts.dev@gmail.com', null=False, blank=False)
    street = models.CharField(
        max_length=255, null=True, blank=True)
    city = models.CharField(
        max_length=50, default='Bahawalpur', null=False, blank=False)
    state = models.CharField(
        max_length=50, default='Bahawalpur', null=True, blank=True)
    zip_code = models.CharField(
        max_length=10, default='63100', null=True, blank=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False)
    phone = models.CharField(
        max_length=12, null=False, blank=False, unique=True)
    email = models.EmailField(
        default='zeroefforts.dev@gmail.com', null=False, blank=False)
    active = models.BooleanField(
        default=True, null=False, blank=False)
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE)
    manager = models.ForeignKey(
        'self', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False)
    phone = models.CharField(
        max_length=50, null=False, blank=True)
    email = models.EmailField(
        default='zeroefforts.dev@gmail.com', null=False, blank=False)
    street = models.CharField(
        max_length=255, null=True, blank=True)
    city = models.CharField(
        max_length=50, default='Bahawalpur', null=False, blank=False)
    state = models.CharField(
        max_length=50, default='Bahawalpur', null=True, blank=True)
    zip_code = models.CharField(
        max_length=10, default='63100', null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
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
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE)
    staff = models.ForeignKey(
        Staff, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Order_Item(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        null=False, blank=False)
    price = models.FloatField(
        null=False, blank=False)
    discount = models.FloatField(null=False, blank=False, default=0)


class Stock(models.Model):
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        null=False, blank=False)
