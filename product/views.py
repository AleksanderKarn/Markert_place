from rest_framework import generics

from product.models import Product
from product.serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        '''filter by city'''
        city = self.request.query_params.get('city')
        cities = self.request.query_params.getlist("city")
        if cities:
            return Product.objects.filter(provider__contacts__city__in=cities)
        if city:
            return Product.objects.filter(provider__contacts__city=city)
        return Product.objects.all()


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
