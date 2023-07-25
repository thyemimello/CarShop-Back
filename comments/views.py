from rest_framework_simplejwt.authentication import JWTAuthentication
from comments.models import Comment
from rest_framework.generics import  RetrieveUpdateDestroyAPIView, ListCreateAPIView
from comments.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from advertisements.models import Advertisements

# Create your views here.
class CommentPostView(ListCreateAPIView):
    queryset = Advertisements.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        advertisement_id = self.kwargs["pk"]
        advertisement = Advertisements.objects.get(id=advertisement_id)

        serializer.save(advertisement=advertisement, user_comment_id=self.request.user)

    def get_queryset(self):
       advertisement_id = self.kwargs["pk"]

       return Comment.objects.filter(advertisement_id=advertisement_id)
    
class CommentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]