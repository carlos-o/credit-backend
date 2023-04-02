from django.db import models
from django.utils.translation import gettext as _
from bank.models import Bank
from client.models import Client


class Credit(models.Model):
    """
        model to store the credit information of client
    """
    AUTOMOTIVE = "Automotive"
    MORTGAGES = "Mortgages"
    COMMERCIAL = "Commercial"
    TYPE_CREDIT = (
        (AUTOMOTIVE, _('Automotive')),
        (MORTGAGES, _('Mortgages')),
        (COMMERCIAL, _('Commercial'))
    )

    client = models.ForeignKey(Client, related_name='client_credit', on_delete=models.CASCADE, blank=False, null=False)
    bank = models.ForeignKey(Bank, related_name='bank_credit', on_delete=models.CASCADE, blank=False, null=False)
    description = models.TextField(_("description of credit"), blank=False, null=False)
    minimum_payment = models.DecimalField(_('Minimum Payment'), max_digits=10, decimal_places=2, blank=False, null=False)
    maximum_payment = models.DecimalField(_('Maximum Payment'), max_digits=10, decimal_places=2, blank=False, null=False)
    period = models.SmallIntegerField(_("credit period in months"), blank=False, null=False)
    credit_type = models.CharField(_("Credit type"), blank=False, null=False, choices=TYPE_CREDIT, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id)


