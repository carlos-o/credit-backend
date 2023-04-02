from .repositories import ClientRepository
from .validations import ValidatorClient
from rest_framework.serializers import ValidationError


class ClientUseCase:

    def __init__(self, repository: ClientRepository, bank_repository):
        self.repository = repository
        self.bank_repository = bank_repository

    def set_params(self, data: dict, pk=None):
        """
            instance data in use case
        """
        self.data = data
        self.pk = pk
        return self

    def execute_store(self):
        """
            execute process to store client information
        """
        self.validate_create()
        client = self.repository.store(self.data)
        return client

    def execute_update(self):
        """
            execute process to update client information
        """
        self.validate()
        client = self.repository.update(self.data, self.pk)
        return client

    def validate(self):
        """
            validate data
        """
        validator = ValidatorClient(self.data)
        if validator.validation() is False:
            errors = validator.mistakes()
            raise ValidationError(errors)
        # check  if a bank with this id exists
        try:
            self.bank_repository.retrieve(self.data.get('bank'))
        except Exception as e:
            raise ValidationError({"bank": str(e)})

    def validate_create(self):
        self.validate()
        # check email
        if self.repository.check_email_exist(self.data.get('email')):
            raise ValidationError({"email": "email exists please use other"})
