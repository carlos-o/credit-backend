from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.serializers import ValidationError
from utils.pagination import CustomPagination
from .serializers import CreditSerializer
from .repositories import CreditRepository
from .usecases import CreditUseCase
from .tasks import send_notification
from bank.repositories import BankRepository
from client.repositories import ClientRepository


class CreditListCreateView(ListCreateAPIView):
    serializer_class = CreditSerializer
    pagination_class = CustomPagination
    permission_classes = (permissions.AllowAny,)

    def repository(self):
        return CreditRepository()

    def get_queryset(self):
        repository = self.repository()
        return repository.list()

    def create(self, request, *args, **kwargs):
        repository = self.repository()
        use_case = CreditUseCase(repository, BankRepository(), ClientRepository()).set_params(self.request.data)
        try:
            credit = use_case.execute_store()
        except ValidationError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = self.get_serializer(credit, many=False).data
        send_notification.delay(serializer.get('client').get('email'))
        return Response(serializer, status=status.HTTP_201_CREATED)
