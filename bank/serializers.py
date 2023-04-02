from rest_framework import serializers


class BankSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    bank_type = serializers.CharField()
    address = serializers.CharField()
    created_at = serializers.DateTimeField()
