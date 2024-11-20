from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.OrderListView.as_view(), name='order_list'),
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('delete/<int:pk>/', views.DeleteOrderView.as_view(), name='order_delete')
]
