import requests

def fetch_book_data(title):
    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}&langRestrict=ko"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("🔍 전체 응답:", data)  # ✅ 여기에 전체 JSON 출력

    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            book = data["items"][0].get("volumeInfo", {})
            return {
                "title": book.get("title", "제목 없음"),
                "authors": ", ".join(book.get("authors", ["저자 정보 없음"])),
                "published_date": book.get("publishedDate", "출판일 정보 없음"),
                "description": book.get("description", "설명 없음"),
                "thumbnail": book.get("imageLinks", {}).get("thumbnail", "")
            }
    return None
