from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.serializers import ValidationError
from utils.pagination import CustomPagination
from .serializers import ClientSerializer
from .repositories import ClientRepository
from .usecases import ClientUseCase
from bank.repositories import BankRepository


class ClientListCreateView(ListCreateAPIView):
    serializer_class = ClientSerializer
    pagination_class = CustomPagination
    permission_classes = (permissions.AllowAny,)

    def repository(self):
        return ClientRepository()

    def get_queryset(self):
        repository = self.repository()
        return repository.list()

    def create(self, request, *args, **kwargs):
        repository = self.repository()
        use_case = ClientUseCase(repository, BankRepository()).set_params(self.request.data)
        try:
            client = use_case.execute_store()
        except ValidationError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = self.get_serializer(client, many=False).data
        return Response(serializer, status=status.HTTP_201_CREATED)


class ClientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    permission_classes = (permissions.AllowAny,)

    def repository(self):
        return ClientRepository()

    def get_object(self):
        pk = self.kwargs.get('pk')
        repository = self.repository()
        return repository.retrieve(pk)

    def update(self, request, *args, **kwargs):
        repository = self.repository()
        use_case = ClientUseCase(repository, BankRepository()).set_params(self.request.data, self.kwargs.get('pk'))
        try:
            client = use_case.execute_update()
        except ValidationError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = self.get_serializer(client, many=False).data
        return Response(serializer, status=status.HTTP_200_OK)
