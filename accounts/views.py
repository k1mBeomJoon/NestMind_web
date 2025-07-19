from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from accounts.forms import SignupForm
from django.contrib.auth import views as auth_views
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 성공 후 login_real 페이지로 리다이렉트
            messages.success(request, '회원가입이 완료되었습니다! 로그인해주세요.')
            return redirect('accounts:login_real')
        else:
            # 폼 에러가 있는 경우
            if form.errors:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_choice(request: HttpRequest):
    if request.GET.get('real') == '1':
        return auth_views.LoginView.as_view(template_name='accounts/login_real.html')(request)
    return render(request, 'accounts/login.html')

def login_real(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{user.first_name or user.username}님, 환영합니다!')
                return redirect('/')  # 메인 페이지로 리다이렉트
            else:
                messages.error(request, 'ID 또는 비밀번호가 올바르지 않습니다.')
        else:
            messages.error(request, 'ID와 비밀번호를 모두 입력해주세요.')
    
    return render(request, 'accounts/login_real.html')

def logout_view(request):
    logout(request)
    messages.success(request, '로그아웃되었습니다.')
    return redirect('/')

@csrf_exempt
def check_duplicate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        field_type = data.get('type')  # 'username' or 'nickname'
        value = data.get('value', '').strip()
        
        if not value:
            return JsonResponse({'success': False, 'message': '값을 입력해주세요.'})
        
        # 중복 검사
        if field_type == 'username':
            # User 모델에서 username 중복 검사
            if User.objects.filter(username=value).exists():
                return JsonResponse({'success': False, 'message': '이미 사용 중인 ID입니다.'})
            else:
                return JsonResponse({'success': True, 'message': '사용 가능한 ID입니다.'})
        
        elif field_type == 'nickname':
            # 여기서는 User 모델의 first_name을 nickname으로 사용한다고 가정
            # 실제로는 별도의 Profile 모델이 있다면 그 모델에서 검사
            if User.objects.filter(first_name=value).exists():
                return JsonResponse({'success': False, 'message': '이미 사용 중인 닉네임입니다.'})
            else:
                return JsonResponse({'success': True, 'message': '사용 가능한 닉네임입니다.'})
        
        else:
            return JsonResponse({'success': False, 'message': '잘못된 필드 타입입니다.'})
    
    return JsonResponse({'success': False, 'message': '잘못된 요청입니다.'})