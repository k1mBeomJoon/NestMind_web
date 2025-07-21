from django.shortcuts import render, redirect, get_object_or_404
from .models import QnAQuestion, QnAComment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
def love_type_test(request):
    return render(request, 'pages/love_type_test.html')

def emotion_style_test(request):
    return render(request, 'pages/emotion_style_test.html')

def personality_test(request):
    return render(request, 'pages/personality_test.html')

def mental_health_test(request):
    return render(request, 'pages/mental_health_test.html')

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
    return render(request, 'pages/faq.html')

def one_on_one_inquiry(request):
    return render(request, 'pages/one_on_one_inquiry.html')

def notice(request):
    return render(request, 'pages/notice.html')

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
