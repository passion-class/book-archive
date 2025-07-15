import json
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookSearchForm
from .models import Book
from .utils import fetch_book_data
from django.contrib import messages
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import escapejs
from django.forms.models import model_to_dict


@login_required
def search_book(request): # 책 검색 기능
    form = BookSearchForm()
    results = []
    books = []
    book_data_json = "[]"
    searched = False
    print("[DEBUG] book_data_json:", book_data_json)

    if request.method == 'POST':
        # 🗑 삭제 처리
        if 'delete' in request.POST:
            title = request.POST.get('title', '').strip()
            deleted_books = Book.objects.filter(title__icontains=title)
            if deleted_books.exists():
                count = deleted_books.count()
                deleted_books.delete()
                messages.success(request, f"{count}권의 책이 삭제되었습니다")
            else:
                messages.error(request, '해당 제목의 책이 존재하지 않습니다')
            return redirect('search_book')

    #검색 처리
        elif 'search' in request.POST:
            form = BookSearchForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title'].strip()
                searched = True
            else:
                title = ''

            if not title:
                books = Book.objects.all()
                book_data_json = json.dumps([model_to_dict(book) for book in books], ensure_ascii=False, default=str)
            else:
                books_qs = Book.objects.filter(title__icontains=title)
                if books_qs.exists():
                    books = books_qs
                    book_data_json = json.dumps(
                        [model_to_dict(book) for book in books],
                        ensure_ascii=False, default=str
                    )
                else:
                    data = fetch_book_data(title)
                    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                            books = [
                                Book(
                                    title=item.get("title", ""),
                                    authors=item.get("authors", ""),
                                    published_date=item.get("published_date", ""),
                                    description=item.get("description", ""),
                                    thumbnail=item.get("thumbnail", ""),
                                    isbn=item.get("isbn", ""),
                                    publisher=item.get("publisher", "")
                                ) for item in data
                            ]
                            book_data_json = json.dumps(data, ensure_ascii=False, default=str)
                    else:
                        books = []
                        book_data_json = "[]"
                        messages.error(request, 'API에 책 정보를 불러올 수 없습니다')

            print("[DEBUG] books:", books)
            if isinstance(books, list):
                print("[DEBUG] books count:", len(books))
            else:
                print("[DEBUG] books count:", books.count())

    return render(request, 'search.html', {
        'form': form,
        'books': books,
        'searched': searched,
        'book_data_json': book_data_json


    })

@login_required
def book_list(request): # 등록된 책 목록 확인 페이지
    books = Book.objects.filter(user=request.user)
    num = [0]
    return render(request, 'book_list.html', {'books': books, 'num': num})

@login_required
@csrf_exempt
def save_selected_books(request): # 책 데이터 저장
    if request.method == 'POST':
        selected_isbns = request.POST.getlist('selected_books')
        book_data_json =request.POST.get('book_data_json')
        print("[DEBUG] book_data_json:", book_data_json if book_data_json else "비어 있음")
        print("book_data_json (raw):", book_data_json)
        print("선택된 인덱스:", selected_isbns)
        print("원본 JSON:", book_data_json)
        print("RAW JSON 확인:", book_data_json)
        print("[DEBUG] 받은 book_data_json:", book_data_json)  # ← 여기가 항상 ""이면 위 문제임

        if not book_data_json:
            messages.error(request, '책 데이터가 전달되지 않습니다')
            return redirect('search_book')

        try:
            book_data = json.loads(book_data_json)
        except json.JSONDecodeError as e:
            print("json decode Error:", e)
            messages.error(request, '책 데이터 파싱오류')
            return redirect('search_book')

        for data in book_data:
            isbn=data.get("isbn", "")
            if isbn in selected_isbns:
                Book.objects.get_or_create(
                    isbn=isbn,
                    user=request.user,
                    defaults={
                        'title': data.get('title', ''),
                        'authors': data.get('authors', ''),
                        'published_date': data.get('published_date', ''),
                        'thumbnail': data.get('thumbnail', ''),
                        'publisher': data.get('publisher', '미상')
                    }
                )

        messages.success(request, f"{len(selected_isbns)}개의 책이 저장되었습니다")
        return redirect('book:book_list')









