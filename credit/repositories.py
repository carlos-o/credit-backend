from .models import Credit


class CreditRepository:

    def list(self) -> list:
        """
            get al bank
            :return: list of bank
        """
        return Credit.objects.order_by('-id')

    def store(self, data: dict) -> Credit:
        """
            store a credit
            :param data: credit information
            :type data: dict
            :return: credit instance
        """
        credit = Credit.objects.create(
            client_id=data.get('client'),
            bank_id=data.get('bank'),
            description=data.get('description'),
            minimum_payment=data.get('minimum_payment'),
            maximum_payment=data.get('maximum_payment'),
            period=data.get('period'),
            credit_type=data.get('credit_type')
        )
        return credit
