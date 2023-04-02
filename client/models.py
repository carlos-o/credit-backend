from django.db import models
from django.utils.translation import gettext as _
from bank.models import Bank


class Client(models.Model):
    """
        model to store client information
    """
    NATURAL = "Natural"
    JURIDICAL = "Juridical"
    TYPE_PERSON = (
        (NATURAL, _('Natural')),
        (JURIDICAL, _('Juridical'))
    )
    bank = models.ForeignKey(Bank, related_name='bank_client', on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(_("Name"), blank=False, null=False, max_length=50)
    last_name = models.CharField(_("Last Name"), blank=False, null=False, max_length=100)
    date_birth = models.DateField(_("Date of Birth"), blank=False, null=False)
    age = models.SmallIntegerField(_("Age"), blank=True, null=True)
    nationality = models.CharField(_("Nationality"), blank=True, null=True, max_length=100)
    address = models.CharField(_("Address"), blank=True, null=True, max_length=255)
    email = models.CharField(_("Email"), blank=False, null=False, unique=True, max_length=255)
    phone = models.CharField(_("Phone"), blank=False, null=False, max_length=15)
    type_person = models.CharField(_("Type of Person"), blank=False, null=False, choices=TYPE_PERSON, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.name}-{str(self.id)}"



