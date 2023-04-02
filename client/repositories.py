from .models import Client
from django.http import Http404
from rest_framework.serializers import ValidationError


class ClientRepository:

    def retrieve(self, pk: int) -> Client:
        """
            get specific client by id
            :param pk: client ID
            :type pk: int
            :return: client instance
        """
        client = Client.objects.filter(id=pk).first()
        if not client:
            raise Http404("Not Found")
        return client

    def list(self) -> list:
        """
            Get all clients
            :return: list of clients
        """
        return Client.objects.order_by('-id')

    def store(self, data: dict) -> Client:
        """
            store a client
            :param data: client information
            :type data: dict
            :return: client instance
        """
        client = Client.objects.create(
            bank_id=data.get('bank'),
            name=data.get('name'),
            last_name=data.get('last_name'),
            date_birth=data.get('date_birth'),
            age=data.get('age'),
            address=data.get('address'),
            nationality=data.get('nationality'),
            email=data.get('email'),
            type_person=data.get('type_person'),
            phone=data.get('phone')
        )
        return client

    def update(self, data: dict, pk: int) -> Client:
        """
            store a client
            :param data: client information
            :type data: dict
            :param pk: client id
            :type pk: int
            :return: client instance
        """
        client = self.retrieve(pk)
        client_compare = self.check_email_exist(data.get('email'))
        if client_compare:
            if client.email != client_compare.email:
                raise ValidationError({"email": "email exists please use other"})
        client.name = data.get('name')
        client.last_name = data.get('last_name')
        client.date_birth = data.get('date_birth')
        client.age = data.get('age')
        client.address = data.get('address')
        client.nationality = data.get('nationality')
        client.email = data.get('email')
        client.type_person = data.get('type_person')
        client.phone = data.get('phone')
        client.bank_id = data.get('bank')
        client.save()
        return client

    def check_email_exist(self, email: str) -> Client:
        """
            check if email all ready exist in app
            :param email: client email
            :return: client instance
        """
        client = Client.objects.filter(email=email).first()
        return client
