from django.contrib import admin
from .models import Artist, Album, Vendor, IncomeSource, Income, Expense


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Vendor)
admin.site.register(IncomeSource)
admin.site.register(Income)
admin.site.register(Expense)