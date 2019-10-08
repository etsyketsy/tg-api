from django.contrib import admin
from .models import Artist, ArtistLink, Release, ReleaseLink, IncomeSource, Vendor, Income, Expense, Product, ProductVariant


admin.site.register(Artist)
admin.site.register(ArtistLink)
admin.site.register(Release)
admin.site.register(ReleaseLink)
admin.site.register(Vendor)
admin.site.register(IncomeSource)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Product)
admin.site.register(ProductVariant)