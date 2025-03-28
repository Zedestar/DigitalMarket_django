from .  import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index_view'),
    path('product_details/<str:pk>/', views.product_details, name='product_details'),
    path('create_product', views.create_product, name='create_product'),
    path('edit_product/<str:pk>/', views.edit_product, name='edit_product'),
]

