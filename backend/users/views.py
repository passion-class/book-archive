# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializer import SignUpSerializer
#
#
# # 화원가입
# class SignUpView(APIView):
#     def post(self, request):
#         serializer = SignUpSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "회원가입 성공"}, status=201)
#         return Response(serializer.errors, status=400)
# # 회원정보
# class MyInfoView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         return Response({
#             "username": request.user.username,
#             "email" : request.user.email,
#         })
#
# # 로그아웃
# from rest_framework_simplejwt.views import TokenRefreshView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
# class LogoutView(APIView):
#     def post(self, request):
#         try:
#             refresh_token = request.data['refresh']
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response({"message": "로그아웃 성공"}, status=200)
#         except Exception as e:
#             print(e)
#             return Response({"message": "로그아웃 실패"}, status=400)
