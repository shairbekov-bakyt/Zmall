from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from advert.api import serializers
from advert.models import Advert, AdvertImage


class AdvertViewSet(ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = serializers.AdvertCreateSerializer

    def list(self, request):
        adverts = Advert.objects.filter(is_active=True)
        serializer = serializers.AdvertListSerializer(adverts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        advert = Advert.objects.get(id=pk)
        serializer = serializers.AdvertDetailSerializer(advert)
        advert.view += 1
        advert.save()
        return Response(serializer.data)
