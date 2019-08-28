from django.contrib import admin
from .models import Artist, Album, Vendor, IncomeSource, Income, Expense, Product, ProductVariant


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Vendor)
admin.site.register(IncomeSource)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Product)
admin.site.register(ProductVariant)