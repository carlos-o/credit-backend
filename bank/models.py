from django.db import models
from django.utils.translation import gettext as _


class Bank(models.Model):
    """
        Model to store bank information
    """

    PRIVATE = "Private"
    GOVERNMENT = "Government"
    TYPE_BANK = (
        (PRIVATE, _('Private')),
        (GOVERNMENT, _('Government'))
    )

    name = models.CharField(_("Name"), blank=False, null=False, max_length=100)
    bank_type = models.CharField(_("Type"), blank=False, null=False, max_length=30, choices=TYPE_BANK)
    address = models.CharField(_("Address"), blank=True, null=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
