from django.urls import path

from product.views import ProductListView, ProductUpdateAPIView, ProductDestroyAPIView, ProductCreateAPIView, \
    ProductRetriveAPIView

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductRetriveAPIView.as_view(), name='product_view'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
]
