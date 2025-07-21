from django.shortcuts import render, redirect, get_object_or_404
from .models import QnAQuestion, QnAComment, FAQ, Inquiry, Notice, LoveTypeQuestion, LoveTypeTestResult, EmotionStyleQuestion, EmotionStyleTestResult, PersonalityQuestion, PersonalityTestResult, MentalHealthQuestion, MentalHealthTestResult
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

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

def create_report(request):
    return render(request, 'pages/create_report.html')

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
def test_history(request):
    return render(request, 'pages/test_history.html')

def report_view(request):
    return render(request, 'pages/report_view.html')

def question_history(request):
    return render(request, 'pages/question_history.html')

def inquiry_history(request):
    return render(request, 'pages/inquiry_history.html')

def profile(request):
    return render(request, 'pages/profile.html')
