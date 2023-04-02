from django.urls import path
from client import views

urlpatterns = [
    path('', views.ClientListCreateView.as_view(), name='client_list'),
    path('<int:pk>/', views.ClientRetrieveUpdateDestroyAPIView.as_view(), name="client_retrieve")
]
