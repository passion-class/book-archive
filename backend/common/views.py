from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# 로그인
def login_view(request):
    user = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user: # 로그인 기능
            log_in = login(request, user)
            
            messages.success(request, "어서오세요, 당신의 서재에.")
            return redirect("book:book_list")
        else:
            messages.error(request, "아이디와 비밀번호를 다시 확인해주세요.")
            return render(request, 'login.html')
    else: # GET 요청시 페이지 호출
        return render(request, 'login.html')
    
# 로그아웃
def logout_view(request):
    logout(request)
    messages.success(request, "로그아웃되었습니다")
    # return render(request, 'logout.html')
    return redirect("common:login")
    # return redirect('/users/login/') # test
