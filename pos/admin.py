from django.contrib import admin
import .models

# Register your models here.
admin.site.register(home.models.Product)
admin.site.register(home.models.Brand)
admin.site.register(home.models.Category)
admin.site.register(home.models.Customer)
admin.site.register(home.models.Order)
admin.site.register(home.models.Order_Item)
admin.site.register(home.models.Staff)
admin.site.register(home.models.Stock)
admin.site.register(home.models.Store)
