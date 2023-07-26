from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .permissions import IsAccountOwner



class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def perform_create(self, serializer):
    #     address_data = self.request.data.get('address', {})
    #     serializer.save(address=address_data)

    
    
    

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "pk"

    def perform_update(self, serializer):
        address_data = self.request.data.get('address', {})
        serializer.save(address=address_data)