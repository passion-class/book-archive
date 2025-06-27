# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages # 메세지 프레임워크
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from users.forms import CreateUser

# import ipdb

# 회원 가입
def signup_view(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid(): # 데이터 유효하면 사용자 정보 db 저장
            print('조건 충족')
            # ipdb.set_trace() # 폼 유효성 검사 후 디버거 실행
            form.save()
            print('가입 완료')
            return redirect("login") # 성공시 로그인 페이지로 이동
        else:
            messages.error(request, '입력 정보를 다시 확인해주세요.')
            return render(request, 'signup.html', {'form': form}) # 에러 문장 출력 및 재 작성 위한 폼 출력
    else: # GET 요청
        form = CreateUser() # 회원가입 form 생성
        return render(request, 'signup.html', {'form':form})
    
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