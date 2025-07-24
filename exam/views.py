from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import LoveTypeQuestion, LoveTypeTestResult, EmotionStyleQuestion, EmotionStyleTestResult, PersonalityQuestion, PersonalityTestResult, MentalHealthQuestion, MentalHealthTestResult

# Create your views here.

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
        return render(request, 'exam/love_type_test_result.html', {'score': score})
    return render(request, 'exam/love_type_test.html', {'questions': questions})

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
        return render(request, 'exam/emotion_style_test_result.html', {'score': score})
    return render(request, 'exam/emotion_style_test.html', {'questions': questions})

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
        return render(request, 'exam/personality_test_result.html', {'score': score})
    return render(request, 'exam/personality_test.html', {'questions': questions})

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
        return render(request, 'exam/mental_health_test_result.html', {'score': score})
    return render(request, 'exam/mental_health_test.html', {'questions': questions})

@login_required(login_url='/accounts/login_real/')
def test_history(request):
    user = request.user
    love_type = LoveTypeTestResult.objects.filter(user=user).order_by('-created_at').first()
    emotion_style = EmotionStyleTestResult.objects.filter(user=user).order_by('-created_at').first()
    personality = PersonalityTestResult.objects.filter(user=user).order_by('-created_at').first()
    mental_health = MentalHealthTestResult.objects.filter(user=user).order_by('-created_at').first()
    return render(request, 'exam/test_history.html', {
        'love_type': love_type,
        'emotion_style': emotion_style,
        'personality': personality,
        'mental_health': mental_health,
    })
