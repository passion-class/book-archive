import requests

def fetch_book_data(title):
    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}&langRestrict=ko"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("🔍 전체 응답:", data)  # ✅ 여기에 전체 JSON 출력

        if "items" in data:
            books = []
            for item in data["items"]:
                volume_info = item.get("volumeInfo",{})
                identifiers = volume_info.get("industryIdentifiers", [])
                isbn_13 = next((id["identifier"] for id in identifiers if id["type"] == "ISBN_13"), None)
                isbn_10 = next((id["identifier"] for id in identifiers if id["type"] == "ISBN_10"), None)
                isbn = isbn_13 or isbn_10 or "unknown"


                books.append({
                    "title": volume_info.get("title", "제목 없음"),
                    "authors": ", ".join(volume_info.get("authors", ["저자 정보 없음"])),
                    "published_date": volume_info.get("publishedDate", "출판일 정보 없음"),
                    "description": volume_info.get("description", "설명 없음"),
                    "thumbnail": volume_info.get("imageLinks", {}).get("thumbnail", ""),
                    "isbn": isbn,
                    "publisher": volume_info.get("publisher", "unknown")
                })
            return books
        else:
            print("item 키가 응답에 없음")
            return []
    else:
        print("APi 요청 실패")
        return []

    return None
