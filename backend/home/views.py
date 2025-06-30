from django.shortcuts import render

# Create your views here.
def home_view(request):
    # return render(request, 'home.html', {'test': '연결 완료'})
    if request.method == 'GET':
        return render(request, 'home.html')
