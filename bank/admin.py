from django.contrib import admin
from bank import models as bank_models


class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bank_type', 'created_at')
    list_filter = ('created_at', 'bank_type',)
    search_fields = ('name',)


admin.site.register(bank_models.Bank, BankAdmin)
