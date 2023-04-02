from rest_framework import serializers
from bank.serializers import BankSerializer
from client.serializers import ClientSerializer


class CreditSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    bank = BankSerializer()
    client = ClientSerializer()
    description = serializers.CharField()
    minimum_payment = serializers.FloatField()
    maximum_payment = serializers.FloatField()
    period = serializers.IntegerField()
    credit_type = serializers.CharField()
    created_at = serializers.DateTimeField()
