from django.urls import path
from bank import views

urlpatterns = [
    path('bank/', views.BankListCreateView.as_view(), name='bank'),
]
