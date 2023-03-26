from django.urls import path

from link_model.views import ProviderListView, ProviderRetriveAPIView, ProviderCreateAPIView, ProviderDestroyAPIView, \
    ProviderUpdateAPIView

urlpatterns = [
    path('provider/', ProviderListView.as_view(), name='provider_list'),
    path('provider/<int:pk>/',ProviderRetriveAPIView.as_view(), name='provider_view'),
    path('provider/create/', ProviderCreateAPIView.as_view(), name='provider_create'),
    path('provider/delete/<int:pk>/', ProviderDestroyAPIView.as_view(), name='provider_delete'),
    path('provider/update/<int:pk>/', ProviderUpdateAPIView.as_view(), name='provider_update'),
]

