from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('love-type-test/', views.love_type_test, name='love_type_test'),
    path('emotion-style-test/', views.emotion_style_test, name='emotion_style_test'),
    path('personality-test/', views.personality_test, name='personality_test'),
    path('mental-health-test/', views.mental_health_test, name='mental_health_test'),
    path('test-history/', views.test_history, name='test_history'),
] 