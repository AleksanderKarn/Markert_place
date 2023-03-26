from django.urls import path

from contacts.views import ContactListView, ContactUpdateAPIView, ContactDestroyAPIView, ContactCreateAPIView, \
    ContactRetriveAPIView

urlpatterns = [
    path('contact/', ContactListView.as_view(), name='contact_list'),
    path('contact/<int:pk>/', ContactRetriveAPIView.as_view(), name='contact_view'),
    path('contact/create/', ContactCreateAPIView.as_view(), name='contact_create'),
    path('contact/delete/<int:pk>/', ContactDestroyAPIView.as_view(), name='contact_delete'),
    path('contact/update/<int:pk>/', ContactUpdateAPIView.as_view(), name='contact_update'),
]
