from django.urls import path
from . import views



urlpatterns = [
    path("comment/<int:pk>/", views.CommentPostView.as_view()),
    path("comment/<int:pk>/update", views.CommentRetrieveUpdateDestroyView.as_view()),    
]

