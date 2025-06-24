import csv
import os

from django.shortcuts import render
from .models import User
from django.conf import settings

def hello_view(request):
    return render(request, 'hello.html')

def result_view(request):
    name = request.GET.get('name')
    if name:
        # 登録
        User.objects.create(user_name=name)

    # 全ユーザー取得
    users = User.objects.all()

    # CSVファイルへの書き込み
    csv_file_path = os.path.join(settings.BASE_DIR, 'users.csv')
    with open(csv_file_path, mode='w', newline='', encoding='cp932') as csvfile:
        writer = csv.writer(csvfile)
        # ヘッダー行（必要に応じてフィールド名を追加）
        writer.writerow(['ユーザー名'])
        # データ行
        for user in users:
            writer.writerow([user.user_name])

    return render(request, 'result.html', {'users': users})
