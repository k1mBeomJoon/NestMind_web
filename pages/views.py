from django.shortcuts import render, redirect, get_object_or_404
from .models import FAQ, Notice
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Max
from django.http import HttpResponseForbidden
from exam.models import (
    LoveTypeTestResult,
    EmotionStyleTestResult,
    PersonalityTestResult,
    MentalHealthTestResult,
)

# Report 모델이 있다고 가정하고 임시로 사용
# from .models import Report

def mainpage(request):
    return render(request, 'pages/mainpage.html')

# 정신건강 정보
def stress_info(request):
    return render(request, 'pages/info/stress_info.html')

def anxiety_info(request):
    return render(request, 'pages/info/anxiety_info.html')

def depression_info(request):
    return render(request, 'pages/info/depression_info.html')

def psychosis_info(request):
    return render(request, 'pages/info/psychosis_info.html')

def burnout_info(request):
    return render(request, 'pages/info/burnout_info.html')

def self_esteem_info(request):
    return render(request, 'pages/info/self_esteem_info.html')

def emotion_record_info(request):
    return render(request, 'pages/info/emotion_record_info.html')

def addiction_info(request):
    return render(request, 'pages/info/addiction_info.html')

def sleep_appetite_info(request):
    return render(request, 'pages/info/sleep_appetite_info.html')

# 자가 관리 방법
def stress_management(request):
    return render(request, 'pages/manage/stress_management.html')

def anxiety_management(request):
    return render(request, 'pages/manage/anxiety_management.html')

def depression_management(request):
    return render(request, 'pages/manage/depression_management.html')

def psychosis_management(request):
    return render(request, 'pages/manage/psychosis_management.html')

def burnout_management(request):
    return render(request, 'pages/manage/burnout_management.html')

def self_esteem_management(request):
    return render(request, 'pages/manage/self_esteem_management.html')

def emotion_record_management(request):
    return render(request, 'pages/manage/emotion_record_management.html')

def addiction_management(request):
    return render(request, 'pages/manage/addiction_management.html')

def sleep_appetite_management(request):
    return render(request, 'pages/manage/sleep_appetite_management.html')

# 검사 / 리포트
# (report 관련 뷰 함수는 report 앱으로 이동)

# 질문 / 답변
# (QnA 관련 뷰 함수는 qna 앱으로 이동)

# ABOUT US
def nestmind(request):
    return render(request, 'pages/aboutus/nestmind.html')

def company_history(request):
    return render(request, 'pages/aboutus/company_history.html')

# 고객지원
# (inquiry 관련 뷰 함수는 inquiry 앱으로 이동)

def faq(request):
    faqs = FAQ.objects.all().order_by('-created_at')
    return render(request, 'pages/customerSupport/faq.html', {'faqs': faqs})

def notice(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'pages/customerSupport/notice.html', {'notices': notices})

# 마이 페이지
@login_required(login_url='/accounts/login_real/')
def profile(request):
    user = request.user
    recent_love_type = LoveTypeTestResult.objects.filter(user=user).order_by('-created_at').first()
    recent_emotion_style = EmotionStyleTestResult.objects.filter(user=user).order_by('-created_at').first()
    recent_personality = PersonalityTestResult.objects.filter(user=user).order_by('-created_at').first()
    recent_mental_health = MentalHealthTestResult.objects.filter(user=user).order_by('-created_at').first()
    recent_report = user.reports.order_by('-created_at').first()
    recent_report_type = recent_report.report_type.type_code if recent_report else None
    recent_report_type_name = recent_report.report_type.type_name if recent_report else None
    return render(request, 'pages/mypage/profile.html', {
        'user': user,
        'recent_love_type': recent_love_type,
        'recent_emotion_style': recent_emotion_style,
        'recent_personality': recent_personality,
        'recent_mental_health': recent_mental_health,
        'recent_report_type': recent_report_type,
        'recent_report_type_name': recent_report_type_name,
    })
