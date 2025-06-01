from django.shortcuts import render
from .models import Name

def hello_view(request):
    return render(request, 'hello.html')

def result_view(request):
    name_text = request.GET.get('name')  # ← GETで取得
    if name_text:
        name_obj = Name.objects.create(text=name_text)  # ← データベースに保存
        return render(request, 'result.html', {'name': name_obj.text})
    else:
        return render(request, 'result.html', {'name': '名前が指定されていません'})
