from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

# 정신건강 정보
def stress_info(request):
    return render(request, 'pages/stress_info.html')

def anxiety_info(request):
    return render(request, 'pages/anxiety_info.html')

def depression_info(request):
    return render(request, 'pages/depression_info.html')

def psychosis_info(request):
    return render(request, 'pages/psychosis_info.html')

def burnout_info(request):
    return render(request, 'pages/burnout_info.html')

def self_esteem_info(request):
    return render(request, 'pages/self_esteem_info.html')

def emotion_record_info(request):
    return render(request, 'pages/emotion_record_info.html')

def addiction_info(request):
    return render(request, 'pages/addiction_info.html')

def sleep_appetite_info(request):
    return render(request, 'pages/sleep_appetite_info.html')

# 자가 관리 방법
def stress_management(request):
    return render(request, 'pages/stress_management.html')

def anxiety_management(request):
    return render(request, 'pages/anxiety_management.html')

def depression_management(request):
    return render(request, 'pages/depression_management.html')

def psychosis_management(request):
    return render(request, 'pages/psychosis_management.html')

def burnout_management(request):
    return render(request, 'pages/burnout_management.html')

def self_esteem_management(request):
    return render(request, 'pages/self_esteem_management.html')

def emotion_record_management(request):
    return render(request, 'pages/emotion_record_management.html')

def addiction_management(request):
    return render(request, 'pages/addiction_management.html')

def sleep_appetite_management(request):
    return render(request, 'pages/sleep_appetite_management.html')

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
def ask_question(request):
    return render(request, 'pages/ask_question.html')

def answer_question(request):
    return render(request, 'pages/answer_question.html')

# ABOUT US
def nestmind_info(request):
    return render(request, 'pages/nestmind_info.html')

def company_history(request):
    return render(request, 'pages/company_history.html')

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
