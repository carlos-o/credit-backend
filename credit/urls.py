from django.urls import path
from credit import views

urlpatterns = [
    path('credit/', views.CreditListCreateView.as_view(), name='credit'),
]
