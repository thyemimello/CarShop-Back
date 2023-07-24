from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementListCreateView(ListCreateAPIView):
    queryset = Advertisement.objects.all().order_by("id")
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdvertisementRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]
