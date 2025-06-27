from django.urls import path
from .views import SignUpView, MyInfoView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView
urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='api-signup'),
    path('my_info/', MyInfoView.as_view(), name='my_info'),
    path('logout/', LogoutView.as_view(), name= "logout")
]