from .repositories import BankRepository
from .validations import ValidatorBank
from rest_framework.serializers import ValidationError


class BankUseCase:

    def __init__(self, repository: BankRepository):
        self.repository = repository

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
        bank = self.repository.store(self.data)
        return bank

    def validate(self):
        """
            validate data
        """
        validator = ValidatorBank(self.data)
        if validator.validation() is False:
            errors = validator.mistakes()
            raise ValidationError(errors)
