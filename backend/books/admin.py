from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin): # admin 페이지 설정
    list_display = ['user', 'title', 'authors', 'publisher'] # admin 페이지에서 제목, 작가 출력 / 출판사 추가?
    # list_filter = [''] # 필터로 걸러줄것들, 필요시 사용
    search_fields = ['title', 'authors'] # 제목, 작가 검색시 조회 가능
    