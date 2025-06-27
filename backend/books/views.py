from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookSearchForm
from .models import Book
from .utils import fetch_book_data
from django.contrib import messages
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


@login_required
def search_book(request):
    form = BookSearchForm()
    result = None
    searched = False

    if request.method == 'POST':
        # 🗑 삭제 처리
        if 'delete' in request.POST:
            title = request.POST.get('title', '').strip()
            print(f"[DEBUG] POST로 받은 title:{title}")
            books = Book.objects.filter(title__icontains=title)

            if not books.exists():
                messages.error(request, " 해당 책이 존재하지 않습니다")
                return redirect('search_book')

            deleted_count, _= books.delete()
            print(f"[DEBUG] 삭제된 책의 개수: {deleted_count}")
            messages.success(request, f" {title} 제목의 책 {deleted_count}개를 삭제했습니다")
            return redirect('search_book')

        # 🔍 검색 또는 등록
        form = BookSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            searched = True

            # DB에서 검색

            result = Book.objects.filter(title__icontains=title).first()

            if not result:
                # 없으면 Google Books API에서 가져오기
                data = fetch_book_data(title)
                if data:
                    result = Book.objects.create(**data)
                else:
                    result = None

    return render(request, 'search.html', {
        'form': form,
        'book': result,
        'searched': searched
    })

@login_required
def book_list(request):
    books = Book.objects.all()
    num = [0]
    return render(request, 'book_list.html', {'books': books, 'num': num})
