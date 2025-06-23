from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookSearchForm
from .models import Book
from .utils import fetch_book_data

def search_book(request):
    form = BookSearchForm()
    result = None
    searched = False

    if request.method == 'POST':
        # 🗑 삭제 처리
        if 'delete' in request.POST:
            title = request.POST.get('title')
            book = get_object_or_404(Book, title=title)
            book.delete()
            return redirect('search_book')

        # 🔍 검색 또는 등록
        form = BookSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            searched = True

            try:
                # DB에서 먼저 검색
                result = Book.objects.get(title__icontains=title)
            except Book.DoesNotExist:
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
