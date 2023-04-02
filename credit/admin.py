from django.contrib import admin
from credit import models as credit_models


class CreditAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'bank', 'credit_type', 'period', 'minimum_payment', 'maximum_payment', 'created_at')
    list_filter = ('created_at', 'credit_type')
    search_fields = ('id', 'client', 'bank',)


admin.site.register(credit_models.Credit, CreditAdmin)
