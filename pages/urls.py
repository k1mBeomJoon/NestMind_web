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
    
    # 질문 / 답변
    
    # ABOUT US
    path('nestmind/', views.nestmind, name='nestmind'),
    path('company-history/', views.company_history, name='company_history'),
    
    # 고객지원
    path('customer-support/faq/', views.faq, name='faq'),
    path('notice/', views.notice, name='notice'),
    
    # 마이 페이지
    path('profile/', views.profile, name='profile'),
]