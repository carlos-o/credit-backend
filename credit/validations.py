from django.utils.translation import gettext as _
from cerberus import Validator
from decimal import Decimal


class ValidatorCredit(Validator):
    """
        Validate class to register a credit.
    """

    schema = {
        'client': {'type': 'integer', 'required': True, 'empty': False},
        'bank': {'type': 'integer', 'required': True, 'empty': False},
        'description': {'type': 'string', 'required': True, 'empty': False},
        'minimum_payment': {'type': 'float', 'required': True, 'empty': False, "decimal": True},
        'maximum_payment': {'type': 'float', 'required': True, 'empty': False, "decimal": True},
        'period': {'type': 'integer', 'required': True, 'empty': False, 'min': 1},
        'credit_type': {'type': 'string', 'required': True, 'empty': False, 'maxlength': 100,
                        'allowed': ['Automotive', 'Commercial', 'Mortgages']},
    }

    def __init__(self, data, *args, **kwargs):
        """
            initialize cerberus with the credit information.

            :param data: credit information.
            :type data: dict.
        """
        super(ValidatorCredit, self).__init__(*args, **kwargs)
        self.data = data
        self.schema = self.__class__.schema

    def validation(self):
        """
            :return: none if data is correct
        """
        return self.validate(self.data, self.schema)

    def _validate_decimal(self, condition, field, value):
        """ Validate the amount have 2 decimal point

        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if condition and value:
            decimal_point = Decimal(str(value))
            if abs(decimal_point.as_tuple().exponent) > 2:
                self._error(field, str(_("The number can not have more than 2 decimal potions")))

    def mistakes(self):
        """
            This method returns the error when, the information sent by the user does not comply
            with the rules in the validation with cerberus

            :return: error of cerberus
        """
        return self.errors
