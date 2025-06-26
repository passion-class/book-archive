from django.urls import path
from .views import SignUpView, MyInfoView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/signup/', SignUpView.as_view(), name='api-signup'),
    path('api/my_info/', MyInfoView.as_view(), name='my_info'),
    path('api/logout/', LogoutView.as_view(), name= "logout")
]