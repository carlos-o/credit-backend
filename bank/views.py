from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.serializers import ValidationError
from utils.pagination import CustomPagination
from .serializers import BankSerializer
from .repositories import BankRepository
from .usecases import BankUseCase


class BankListCreateView(ListCreateAPIView):
    serializer_class = BankSerializer
    pagination_class = CustomPagination
    permission_classes = (permissions.AllowAny,)

    def repository(self) -> BankRepository:
        """
            instance or repository
            :return: BankRepository
        """
        return BankRepository()

    def get_queryset(self):
        """
            :return: list of bank
        """
        repository = self.repository()
        return repository.list()

    def create(self, request, *args, **kwargs):
        repository = self.repository()
        use_case = BankUseCase(repository).set_params(self.request.data)
        try:
            bank = use_case.execute_store()
        except ValidationError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = self.get_serializer(bank, many=False).data
        return Response(serializer, status=status.HTTP_201_CREATED)
