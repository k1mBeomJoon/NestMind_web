from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # 메인 페이지
    path('', views.mainpage, name='mainpage'),
    
    # 정신건강 정보
    path('stress-info/', views.stress_info, name='stress_info'),
    path('anxiety-info/', views.anxiety_info, name='anxiety_info'),
    path('depression-info/', views.depression_info, name='depression_info'),
    path('psychosis-info/', views.psychosis_info, name='psychosis_info'),
    path('burnout-info/', views.burnout_info, name='burnout_info'),
    path('self-esteem-info/', views.self_esteem_info, name='self_esteem_info'),
    path('emotion-record-info/', views.emotion_record_info, name='emotion_record_info'),
    path('addiction-info/', views.addiction_info, name='addiction_info'),
    path('sleep-appetite-info/', views.sleep_appetite_info, name='sleep_appetite_info'),
    
    # 자가 관리 방법
    path('stress-management/', views.stress_management, name='stress_management'),
    path('anxiety-management/', views.anxiety_management, name='anxiety_management'),
    path('depression-management/', views.depression_management, name='depression_management'),
    path('psychosis-management/', views.psychosis_management, name='psychosis_management'),
    path('burnout-management/', views.burnout_management, name='burnout_management'),
    path('self-esteem-management/', views.self_esteem_management, name='self_esteem_management'),
    path('emotion-record-management/', views.emotion_record_management, name='emotion_record_management'),
    path('addiction-management/', views.addiction_management, name='addiction_management'),
    path('sleep-appetite-management/', views.sleep_appetite_management, name='sleep_appetite_management'),
    
    # 검사 / 리포트
    path('love-type-test/', views.love_type_test, name='love_type_test'),
    path('emotion-style-test/', views.emotion_style_test, name='emotion_style_test'),
    path('personality-test/', views.personality_test, name='personality_test'),
    path('mental-health-test/', views.mental_health_test, name='mental_health_test'),
    path('create-report/', views.create_report, name='create_report'),
    
    # 질문 / 답변
    path('ask-question/', views.ask_question, name='ask_question'),
    path('answer-question/', views.answer_question, name='answer_question'),
    
    # ABOUT US
    path('nestmind-info/', views.nestmind_info, name='nestmind_info'),
    path('company-history/', views.company_history, name='company_history'),
    
    # 고객지원
    path('faq/', views.faq, name='faq'),
    path('one-on-one-inquiry/', views.one_on_one_inquiry, name='one_on_one_inquiry'),
    path('notice/', views.notice, name='notice'),
    
    # 마이 페이지
    path('test-history/', views.test_history, name='test_history'),
    path('report-view/', views.report_view, name='report_view'),
    path('question-history/', views.question_history, name='question_history'),
    path('inquiry-history/', views.inquiry_history, name='inquiry_history'),
    path('profile/', views.profile, name='profile'),
]