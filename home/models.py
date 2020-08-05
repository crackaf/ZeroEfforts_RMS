from django.db import models
from django.conf import settings

# Create your models here


class Brand(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    #quantity=models.PositiveIntegerField(null=False, blank=False)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,  null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    createdDate = models.DateTimeField(auto_now=True)
    updatedDate = models.DateTimeField(auto_now=False)
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='%(class)s_product_created')
    updatedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='%(class)s_product_updated')

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=50, null=False,
                            blank=False, unique=True)
    # phone=model.models.PhoneNumberField(_(""))
    email = models.EmailField(
        default='zeroefforts.dev@gmail.com', null=False, blank=False)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(
        max_length=50, default='Bahawalpur', null=False, blank=False)
    state = models.CharField(
        max_length=50, default='Bahawalpur', null=True, blank=True)
    zip_code = models.CharField(
        max_length=10, default='63100', null=True, blank=True)


class Staff(models.Model):
    name = models.CharField(max_length=50, null=False,
                            blank=False, unique=True)
    # phone=model.models.PhoneNumberField(_(""))
    email = models.EmailField(
        default='zeroefforts.dev@gmail.com', null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE)
    # manager = models.ForeignKey(
    #   Staff, on_delete=models.DO_NOTHING)  # on_update=models.DO_NOTHING)


class Customer(models.Model):
    name = models.CharField(max_length=50, null=False,
                            blank=False)
    # phone=model.models.PhoneNumberField(_(""))
    email = models.EmailField(
        default='zeroefforts.dev@gmail.com', null=False, blank=False)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(
        max_length=50, default='Bahawalpur', null=False, blank=False)
    state = models.CharField(
        max_length=50, default='Bahawalpur', null=True, blank=True)
    zip_code = models.CharField(
        max_length=10, default='63100', null=True, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING)  # , on_update=models.CASCADE)

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
        Store, on_delete=models.CASCADE)  # , on_update=models.CASCADE)
    staff = models.ForeignKey(
        Staff, on_delete=models.DO_NOTHING)  # , on_update=models.DO_NOTHING)


class Order_Item(models.Model):
    # order = models.ForeignKey(
    #   Store, on_delete=models.CASCADE)#, on_update=models.CASCADE)
    # item = models.ForeignKey(
    #   Store, on_delete=models.CASCADE)#, on_update=models.CASCADE)
    '''CREATE TABLE sales.order_items(
        order_id INT,
        item_id INT,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        list_price DECIMAL (10, 2) NOT NULL,
        discount DECIMAL (4, 2) NOT NULL DEFAULT 0,
        PRIMARY KEY (order_id, item_id),
        FOREIGN KEY (order_id) 
        REFERENCES sales.orders (order_id) 
        ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (product_id) 
        REFERENCES production.products (product_id) 
        ON DELETE CASCADE ON UPDATE CASCADE
);'''


class Stock(models.Model):
    '''CREATE TABLE production.stocks (
        store_id INT,
        product_id INT,
        quantity INT,
        PRIMARY KEY (store_id, product_id),
        FOREIGN KEY (store_id) 
        REFERENCES sales.stores (store_id) 
        ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (product_id) 
        REFERENCES production.products (product_id) 
        ON DELETE CASCADE ON UPDATE CASCADE
);'''
