from rest_framework import serializers

from link_model.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderNotUpdateArrearsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'type',
            'name',
            'provider',
            'time_create',
            'contacts'
        )