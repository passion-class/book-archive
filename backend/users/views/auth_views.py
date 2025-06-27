from rest_framework import permissions 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from users.serializer import SignUpSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# 회원가입
class SignUpView(APIView):
    # Forbidden (CSRF token missing.) 에러로 인한 설정 추가.
    permission_classes = [permissions.AllowAny] # 인증되지 않은(로그인X) 사용자 접근 가능
    authentication_classes = [] # 세션 인증 제외, 세션 기반 CSRF 검사 적용될 여지 줄이기. 어떠한 인증 방식 요구 X
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공"}, status=201)
        return Response(serializer.errors, status=400)

# 로그아웃
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "로그아웃 성공"}, status=200)
        except Exception as e:
            print(e)
            return Response({"message": "로그아웃 실패"}, status=400)
