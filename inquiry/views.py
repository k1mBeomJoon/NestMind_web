from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Inquiry

# Create your views here.

@login_required(login_url='/accounts/login_real/')
def one_on_one_inquiry(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        Inquiry.objects.create(
            user=request.user,
            category=category,
            title=title,
            content=content
        )
        messages.success(request, '문의가 정상적으로 등록되었습니다.')
        return redirect('inquiry:one_on_one_inquiry')
    categories = Inquiry.CATEGORY_CHOICES
    return render(request, 'inquiry/one_on_one_inquiry.html', {'categories': categories})

@login_required(login_url='/accounts/login_real/')
def inquiry_history(request):
    inquiries = Inquiry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'inquiry/inquiry_history.html', {'inquiries': inquiries})
