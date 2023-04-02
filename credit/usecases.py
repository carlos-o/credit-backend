from .repositories import CreditRepository
from .validations import ValidatorCredit
from rest_framework.serializers import ValidationError


class CreditUseCase:

    def __init__(self, repository: CreditRepository, bank_repository, client_repository):
        self.repository = repository
        self.bank_repository = bank_repository
        self.client_repository = client_repository

    def set_params(self, data: dict):
        """
            instance data in usecase
        """
        self.data = data
        return self

    def execute_store(self):
        """
            execute process to store bank information
        """
        self.validate()
        credit = self.repository.store(self.data)
        return credit

    def validate(self):
        """
            validate data
        """
        validator = ValidatorCredit(self.data)
        if validator.validation() is False:
            errors = validator.mistakes()
            raise ValidationError(errors)
        # check  if a client with this id exists
        try:
            self.client_repository.retrieve(self.data.get('client'))
        except Exception as e:
            raise ValidationError({"client": str(e)})
        # check  if a bank with this id exists
        try:
            self.bank_repository.retrieve(self.data.get('bank'))
        except Exception as e:
            raise ValidationError({"bank": str(e)})
