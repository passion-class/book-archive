from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login, authenticate, logout

# 로그인
def login_view(request):
    user = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user: # 로그인 기능
            log_in = login(request, user)
            return redirect("book:book_list")
        else:
            error = "아이디 또는 비밀번호가 틀렸습니다"
            return render(request, 'login.html', {'error': error})
    else: # GET 요청시 페이지 호출
        return render(request, 'login.html')
    
# 로그아웃
def logout_view(request):
    if request.method == 'POST':
            logout(request)
    # return render(request, 'logout.html')
    return redirect("common:login")
    # return redirect('/users/login/') # test
