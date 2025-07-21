from django.shortcuts import render, redirect, get_object_or_404
from .models import QnAQuestion, QnAComment, FAQ, Inquiry, Notice, LoveTypeQuestion, LoveTypeTestResult, EmotionStyleQuestion, EmotionStyleTestResult, PersonalityQuestion, PersonalityTestResult, MentalHealthQuestion, MentalHealthTestResult, Report, ReportType
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Max
from django.http import HttpResponseForbidden

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
@login_required(login_url='/accounts/login_real/')
def love_type_test(request):
    questions = LoveTypeQuestion.objects.all().order_by('id')[:20]
    if request.method == 'POST':
        answers = []
        score = 0
        for q in questions:
            ans = int(request.POST.get(f'question_{q.id}', 0))
            answers.append(ans)
            score += ans
        LoveTypeTestResult.objects.create(
            user=request.user,
            answers=answers,
            score=score,
            test_type='love_type',
        )
        return render(request, 'pages/test/love_type_test_result.html', {'score': score})
    return render(request, 'pages/test/love_type_test.html', {'questions': questions})

@login_required(login_url='/accounts/login_real/')
def emotion_style_test(request):
    questions = EmotionStyleQuestion.objects.all().order_by('id')[:20]
    if request.method == 'POST':
        answers = []
        score = 0
        for q in questions:
            ans = int(request.POST.get(f'question_{q.id}', 0))
            answers.append(ans)
            score += ans
        EmotionStyleTestResult.objects.create(
            user=request.user,
            answers=answers,
            score=score,
            test_type='emotion_style',
        )
        return render(request, 'pages/test/emotion_style_test_result.html', {'score': score})
    return render(request, 'pages/test/emotion_style_test.html', {'questions': questions})

@login_required(login_url='/accounts/login_real/')
def personality_test(request):
    questions = PersonalityQuestion.objects.all().order_by('id')[:20]
    if request.method == 'POST':
        answers = []
        score = 0
        for q in questions:
            ans = int(request.POST.get(f'question_{q.id}', 0))
            answers.append(ans)
            score += ans
        PersonalityTestResult.objects.create(
            user=request.user,
            answers=answers,
            score=score,
            test_type='personality',
        )
        return render(request, 'pages/test/personality_test_result.html', {'score': score})
    return render(request, 'pages/test/personality_test.html', {'questions': questions})

@login_required(login_url='/accounts/login_real/')
def mental_health_test(request):
    questions = MentalHealthQuestion.objects.all().order_by('id')[:20]
    if request.method == 'POST':
        answers = []
        score = 0
        for q in questions:
            ans = int(request.POST.get(f'question_{q.id}', 0))
            answers.append(ans)
            score += ans
        MentalHealthTestResult.objects.create(
            user=request.user,
            answers=answers,
            score=score,
            test_type='mental_health',
        )
        return render(request, 'pages/test/mental_health_test_result.html', {'score': score})
    return render(request, 'pages/test/mental_health_test.html', {'questions': questions})

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
    return render(request, 'pages/test/create_report.html', {
        'love_type': love_type,
        'emotion_style': emotion_style,
        'personality': personality,
        'mental_health': mental_health,
        'success': success,
    })

# 질문 / 답변

@login_required(login_url='/accounts/login_real/')
def ask_question(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        QnAQuestion.objects.create(
            category=category,
            title=title,
            content=content,
            author=request.user,
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        return redirect('pages:answer_question')
    return render(request, 'pages/qna/ask_question.html')

def answer_question(request):
    category = request.GET.get('category')
    if category:
        questions = QnAQuestion.objects.filter(category=category).order_by('-created_at')
    else:
        questions = QnAQuestion.objects.all().order_by('-created_at')
    return render(request, 'pages/qna/answer_question.html', {'questions': questions, 'selected_category': category})

def question_detail(request, question_id):
    question = get_object_or_404(QnAQuestion, id=question_id)
    comments = question.comments.order_by('created_at')
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('/accounts/login_real/?next=' + request.path)
        content = request.POST.get('comment_content')
        if content:
            QnAComment.objects.create(
                question=question,
                author=request.user,
                content=content,
                created_at=timezone.now(),
            )
            return redirect('pages:question_detail', question_id=question_id)
    return render(request, 'pages/qna/question_detail.html', {'question': question, 'comments': comments})

# ABOUT US
def nestmind(request):
    return render(request, 'pages/aboutus/nestmind.html')

def company_history(request):
    return render(request, 'pages/aboutus/company_history.html')

# 고객지원
def faq(request):
    faqs = FAQ.objects.all().order_by('-created_at')
    return render(request, 'pages/customerSupport/faq.html', {'faqs': faqs})

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
        return redirect('pages:one_on_one_inquiry')
    categories = Inquiry.CATEGORY_CHOICES
    return render(request, 'pages/customerSupport/one_on_one_inquiry.html', {'categories': categories})

def notice(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'pages/customerSupport/notice.html', {'notices': notices})

# 마이 페이지
@login_required(login_url='/accounts/login_real/')
def test_history(request):
    user = request.user
    love_type = LoveTypeTestResult.objects.filter(user=user).order_by('-created_at').first()
    emotion_style = EmotionStyleTestResult.objects.filter(user=user).order_by('-created_at').first()
    personality = PersonalityTestResult.objects.filter(user=user).order_by('-created_at').first()
    mental_health = MentalHealthTestResult.objects.filter(user=user).order_by('-created_at').first()
    return render(request, 'pages/mypage/test_history.html', {
        'love_type': love_type,
        'emotion_style': emotion_style,
        'personality': personality,
        'mental_health': mental_health,
    })

@login_required(login_url='/accounts/login_real/')
def report_view(request):
    reports = Report.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'pages/mypage/report_view.html', {'reports': reports})

@login_required(login_url='/accounts/login_real/')
def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if report.user != request.user:
        return HttpResponseForbidden('이 리포트에 접근할 권한이 없습니다.')
    return render(request, 'pages/report/report_detail.html', {'report': report})

@login_required(login_url='/accounts/login_real/')
def question_history(request):
    questions = QnAQuestion.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'pages/mypage/question_history.html', {'questions': questions})

@login_required(login_url='/accounts/login_real/')
def inquiry_history(request):
    inquiries = Inquiry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'pages/mypage/inquiry_history.html', {'inquiries': inquiries})

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
