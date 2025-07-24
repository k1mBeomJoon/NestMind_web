from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Report, ReportType
from exam.models import LoveTypeTestResult, EmotionStyleTestResult, PersonalityTestResult, MentalHealthTestResult

@login_required(login_url='/accounts/login_real/')
def create_report(request):
    user = request.user
    love_type = LoveTypeTestResult.objects.filter(user=user).order_by('-created_at').first()
    emotion_style = EmotionStyleTestResult.objects.filter(user=user).order_by('-created_at').first()
    personality = PersonalityTestResult.objects.filter(user=user).order_by('-created_at').first()
    mental_health = MentalHealthTestResult.objects.filter(user=user).order_by('-created_at').first()
    success = False
    if request.method == 'POST':
        selected = request.POST.getlist('selected_tests')
        if len(selected) == 4:
            code_map = {}
            if love_type and 'love_type' in selected:
                code_map['love_type'] = 'R' if love_type.score >= 60 else 'A'
            if emotion_style and 'emotion_style' in selected:
                code_map['emotion_style'] = 'B' if emotion_style.score >= 60 else 'S'
            if personality and 'personality' in selected:
                code_map['personality'] = 'O' if personality.score >= 60 else 'C'
            if mental_health and 'mental_health' in selected:
                code_map['mental_health'] = 'I' if mental_health.score >= 60 else 'X'
            type_code = (
                code_map.get('love_type', '') +
                code_map.get('emotion_style', '') +
                code_map.get('personality', '') +
                code_map.get('mental_health', '')
            )
            report_type = ReportType.objects.filter(type_code=type_code).first()
            if report_type:
                Report.objects.create(user=user, report_type=report_type)
                success = True
    return render(request, 'report/create_report.html', {
        'love_type': love_type,
        'emotion_style': emotion_style,
        'personality': personality,
        'mental_health': mental_health,
        'success': success,
    })

@login_required(login_url='/accounts/login_real/')
def report_view(request):
    reports = Report.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'report/report_view.html', {'reports': reports})

@login_required(login_url='/accounts/login_real/')
def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if report.user != request.user:
        return HttpResponseForbidden('이 리포트에 접근할 권한이 없습니다.')
    return render(request, 'report/report_detail.html', {'report': report})
