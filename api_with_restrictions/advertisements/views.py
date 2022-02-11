from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrAdmin, IsDraftStatus
from .models import Advertisement, AdvertisementStatusChoices
from .filters import AdvertisementFilter
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdmin, IsDraftStatus]


    #Вывод всех объявлений без черновиков, черновики возмржно просматривать только создателям
    #по прямому обращению
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.exclude(status=AdvertisementStatusChoices.DRAFT)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)