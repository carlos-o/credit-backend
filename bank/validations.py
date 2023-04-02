from cerberus import Validator
from django.utils.translation import gettext as _


class ValidatorBank(Validator):
    """
        Validate class to register a bank.
    """

    schema = {
        'name': {'type': 'string', 'required': True, 'empty': False, 'minlength': 5, 'maxlength': 100},
        'bank_type': {'type': 'string', 'required': True, 'empty': False, 'maxlength': 30,
                      'allowed': ['Private', 'Government']},
        'address': {'type': 'string', 'required': True, 'empty': False, 'maxlength': 255}
    }

    def __init__(self, data, *args, **kwargs):
        """
            initialize cerberus with the bank information.

            :param data: bank information.
            :type data: dict.
        """
        super(ValidatorBank, self).__init__(*args, **kwargs)
        self.data = data
        self.schema = self.__class__.schema

    def validation(self):
        """
            :return: none if data is correct
        """
        return self.validate(self.data, self.schema)

    def mistakes(self):
        """
            This method returns the error when, the information sent by the user does not comply
            with the rules in the validation with cerberus

            :return: error of cerberus
        """
        return self.errors
