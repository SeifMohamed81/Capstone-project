from django.urls import path,include
from .views import TransactionListCreateView, TransactionDetailView,TransactionViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    
    path('users/', UserListView.as_view(), name='user-list'),

    path('users/<int:user_id>/transactions/', UserTransactionsView.as_view(), name='user-transactions'),
    
    path('reports/', FinancialReportsView.as_view(), name='reports'),
    path('', include(router.urls)),

]
