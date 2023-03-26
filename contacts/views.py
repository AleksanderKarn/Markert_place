from rest_framework import generics

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactListView(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactCreateAPIView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
