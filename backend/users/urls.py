from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    # path("login/", views.login_view, name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("info/", views.my_info_view, name="info"),
    ]