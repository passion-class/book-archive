from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
from .views import signup_view, login_view, logout_view, my_info_view

app_name = 'users'

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("my_info/", views.my_info_view, name="my_info"),
    ]