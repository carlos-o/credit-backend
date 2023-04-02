from .models import Bank
from django.http import Http404


class BankRepository:

    def retrieve(self, pk: int) -> Bank:
        """
            get specific bank by id
            :param pk: bank id
            :type pk: int
            :return: bank instance
        """
        bank = Bank.objects.filter(id=pk).first()
        if not bank:
            raise Http404("Not Found")
        return bank

    def list(self) -> list:
        """
            Get all bank
            :return: list of bank
        """
        return Bank.objects.order_by('-id')

    def store(self, data: dict) -> Bank:
        """
            store a bank
            :param data: bank information
            :type data: dict
            :return: Bank instance
        """
        bank = Bank.objects.create(**data)
        return bank
