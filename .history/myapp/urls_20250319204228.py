from .  import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index_view'),
    path('product_details/<str:pk>/', views.product_details, name='product_details'),
]

