from django.shortcuts import render
from .models import User

def hello_view(request):
    return render(request, 'hello.html')

def result_view(request):
    name = request.GET.get('name')
    if name:
        # 登録
        User.objects.create(user_name=name)

    # 全ユーザー取得
    users = User.objects.all()
    return render(request, 'result.html', {'users': users})
