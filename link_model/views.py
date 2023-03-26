from rest_framework import generics

from link_model.models import Provider
from link_model.serializers import ProviderSerializer, ProviderNotUpdateArrearsSerializer


class ProviderListView(generics.ListAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ProviderCreateAPIView(generics.CreateAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ProviderDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ProviderUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProviderNotUpdateArrearsSerializer
    queryset = Provider.objects.all()


class ProviderRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
