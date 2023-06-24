from django.contrib import admin
from .models import *

# username: admin password:admin
# username: customer1 password:user1234
# username: supplier1 password:user1234


# Register your models here.


admin.site.register(Customer)


admin.site.register(Supplier)


admin.site.register(Order)


admin.site.register(OrderItem)


admin.site.register(ShippingAddress)


class ProductSizesAdmin(admin.StackedInline):
    model = ProductSizes
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizesAdmin, ]


admin.site.register(Product, ProductAdmin)
