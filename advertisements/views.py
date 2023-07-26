from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.models import User
from .models import Advertisements
from .serializers import AdvertusementsSerializer


class AdvertisementListCreateView(ListCreateAPIView):
    queryset = Advertisements.objects.all().order_by("id")
    serializer_class = AdvertusementsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)       
        


class AdvertisementRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Advertisements.objects.all()
    serializer_class = AdvertusementsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    
