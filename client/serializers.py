from rest_framework import serializers
from bank.serializers import BankSerializer


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    date_birth = serializers.DateField()
    age = serializers.IntegerField()
    address = serializers.CharField()
    nationality = serializers.CharField()
    email = serializers.CharField()
    type_person = serializers.CharField()
    phone = serializers.CharField()
    created_at = serializers.DateTimeField()
    bank = BankSerializer()