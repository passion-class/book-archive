from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

app_name = 'users'

app_name = 'users'

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("info/", views.my_info_view, name="info"),
    ]