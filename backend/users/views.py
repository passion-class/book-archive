from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView




def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, '/users/signup.html', {'form': form})
    # 회원정보
def my_info_view(request):
    return render(request, "users/my_info.html", {
        "username": request.user.username,
        "email": request.user.email,
    })
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("my_info/")
        else:
            error = "아이디 또는 비밀번호가 틀렷습니다"
            return render(request, 'users/login.html', {'error': error})
        return render(requset, 'users/login.html')

    # 로그아웃
def logout_view(request):
        logout(request)
        return redirect("login/")