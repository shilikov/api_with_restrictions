from django_filters import rest_framework as filters, DateTimeFromToRangeFilter


from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_at = DateTimeFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ["created_at", "status"]