from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from accounts.forms import SignupForm
from django.contrib.auth import views as auth_views
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
import json
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 닉네임 중복 최종 확인
            from accounts.models import Profile
            nickname = form.cleaned_data['nickname']
            if Profile.objects.filter(nickname=nickname).exclude(user=user).exists():
                user.delete()  # 회원가입 취소
                messages.error(request, '이미 사용 중인 닉네임입니다. 다른 닉네임을 입력해주세요.')
                return redirect('accounts:signup')
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
                # 로그인 환영 메시지
                messages.success(request, f'{user.profile.nickname or user.username}님, 환영합니다!')
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
            # Profile.nickname 중복 검사
            from accounts.models import Profile
            if Profile.objects.filter(nickname=value).exists():
                return JsonResponse({'success': False, 'message': '이미 사용 중인 닉네임입니다.'})
            else:
                return JsonResponse({'success': True, 'message': '사용 가능한 닉네임입니다.'})
        
        else:
            return JsonResponse({'success': False, 'message': '잘못된 필드 타입입니다.'})
    
    return JsonResponse({'success': False, 'message': '잘못된 요청입니다.'})

@csrf_exempt
@login_required
def change_nickname(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_nickname = data.get('nickname', '').strip()
        if not new_nickname:
            return JsonResponse({'success': False, 'message': '닉네임을 입력해주세요.'})
        from accounts.models import Profile
        if Profile.objects.filter(nickname=new_nickname).exclude(user=request.user).exists():
            return JsonResponse({'success': False, 'message': '이미 사용 중인 닉네임입니다.'})
        # user.profile.nickname에 저장
        request.user.profile.nickname = new_nickname
        request.user.profile.save()
        return JsonResponse({'success': True, 'message': '닉네임이 변경되었습니다.'})
    return JsonResponse({'success': False, 'message': '잘못된 요청입니다.'})

@csrf_exempt
@login_required
def change_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        current = data.get('current_password', '')
        new = data.get('new_password', '')
        new2 = data.get('new_password2', '')
        if not (current and new and new2):
            return JsonResponse({'success': False, 'message': '모든 항목을 입력해주세요.'})
        if new != new2:
            return JsonResponse({'success': False, 'message': '새 비밀번호가 일치하지 않습니다.'})
        if not request.user.check_password(current):
            return JsonResponse({'success': False, 'message': '현재 비밀번호가 올바르지 않습니다.'})
        # 비밀번호 유효성 검사(간단 예시)
        if len(new) < 8 or len(new) > 20:
            return JsonResponse({'success': False, 'message': '비밀번호는 8~20자여야 합니다.'})
        if request.user.username in new or request.user.first_name in new:
            return JsonResponse({'success': False, 'message': '아이디/닉네임을 포함할 수 없습니다.'})
        if any(new.count(c*3) > 0 for c in set(new)):
            return JsonResponse({'success': False, 'message': '동일한 문자/숫자 3회 이상 반복 불가.'})
        request.user.set_password(new)
        request.user.save()
        update_session_auth_hash(request, request.user)
        return JsonResponse({'success': True, 'message': '비밀번호가 변경되었습니다.'})
    return JsonResponse({'success': False, 'message': '잘못된 요청입니다.'})

@csrf_exempt
@login_required
def withdraw(request):
    if request.method == 'POST':
        user = request.user
        from django.contrib.auth import logout
        logout(request)
        user.delete()
        return JsonResponse({'success': True, 'message': '회원 탈퇴가 완료되었습니다.'})
    return JsonResponse({'success': False, 'message': '잘못된 요청입니다.'})