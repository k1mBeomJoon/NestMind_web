from django.urls import path
from . import views

app_name = 'qna'

urlpatterns = [
    path('ask-question/', views.ask_question, name='ask_question'),
    path('answer-question/', views.answer_question, name='answer_question'),
    path('question-detail/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question-history/', views.question_history, name='question_history'),
] 