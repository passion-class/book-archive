from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
from .views import signup_view, my_info_view, logout_view

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout_view"),
    path("my_info/", views.my_info_view, name="my_info"),
    ]