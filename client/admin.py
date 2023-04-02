from django.contrib import admin
from client import models as client_models


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'bank', 'date_birth', 'email', 'type_person', 'created_at')
    list_filter = ('created_at', 'type_person')
    search_fields = ('name', 'email', 'bank')


admin.site.register(client_models.Client, ClientAdmin)
