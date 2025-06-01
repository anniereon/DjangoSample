from django.shortcuts import render

def hello_view(request):
    return render(request, 'hello.html')

def result_view(request):
    name = request.GET.get('name')  # フォームからのGETデータを取得
    return render(request, 'result.html', {'name': name})
