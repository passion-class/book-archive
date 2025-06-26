from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from users.serializer import SignUpSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# 화원가입
class SignUpView(APIView):
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
