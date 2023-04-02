from cerberus import Validator
from django.utils.translation import gettext as _
import re


class ValidatorClient(Validator):
    """
        Validate class to register a bank.
    """

    schema = {
        'bank': {'type': 'integer', 'required': True, 'empty': False},
        'name': {'type': 'string', 'required': True, 'empty': False, 'minlength': 2, 'maxlength': 50},
        'last_name': {'type': 'string', 'required': True, 'empty': False, 'minlength': 2, 'maxlength': 100},
        'date_birth': {'type': 'string', 'required': True, 'empty': False, 'birthday': True},
        'age': {'type': 'integer', 'required': False, 'empty': False, 'min': 1, 'max': 99},
        'nationality': {'type': 'string', 'required': False, 'empty': False, 'minlength': 5, 'maxlength': 100},
        'address': {'type': 'string', 'required': False, 'empty': False, 'minlength': 5, 'maxlength': 255},
        'email': {'type': 'string', 'required': True, 'empty': False, 'maxlength': 255, 'mail': True},
        'phone': {'type': 'string', 'required': True, 'empty': False, 'minlength': 7, 'maxlength': 16},
        'type_person': {'type': 'string', 'required': True, 'empty': False, 'maxlength': 50,
                        'allowed': ['Natural', 'Juridical']},
    }

    def __init__(self, data, *args, **kwargs):
        """
            initialize cerberus with the bank information.

            :param data: bank information.
            :type data: dict.
        """
        super(ValidatorClient, self).__init__(*args, **kwargs)
        self.data = data
        self.schema = self.__class__.schema

    def validation(self):
        """
            :return: none if data is correct
        """
        return self.validate(self.data, self.schema)

    def _validate_birthday(self, birthday, field, date):
        """ Validate the user's birthday

        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if birthday:
            date = date[:10]
            if not re.match(r'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))', date):
                self._error(field, str(_("The date you entered is not valid")))

    def _validate_mail(self, mail, field, value):
        """ Validate the client's email

        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if mail and value:
            if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', value):
                self._error(field, str(_("Please enter a valid email address")))
            elif len(value.split("@")[0]) >= 64:
                self._error(field, str(_("Invalid email")))
            elif len(value.split("@")[1].split(".")[0]) >= 255:
                self._error(field, str(_("Invalid email")))

    def mistakes(self):
        """
            This method returns the error when, the information sent by the user does not comply
            with the rules in the validation with cerberus

            :return: error of cerberus
        """
        return self.errors
