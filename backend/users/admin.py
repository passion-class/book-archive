from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # User 모델 기본 관리자 셋 충돌 방지 위한 BaseUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model() # User 모델 클래스 가져옴

admin.site.unregister(User) # 기존 User 모델 등록 해제

@admin.register(User) # 해제 후 다시 등록
class UserAdmin(BaseUserAdmin): # admin 페이지 설정
    list_display = ['username', 'email'] 
    # list_filter = [] # 필터로 걸러줄것들, 필요시 사용
    search_fields = ['username', 'email'] 