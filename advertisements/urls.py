from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("advertisements/", views.AdvertisementListCreateView.as_view()),
    path("advertisements/<int:pk>", views.AdvertisementRetrieveUpdateDestroyView.as_view())
]
