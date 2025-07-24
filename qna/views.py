from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import QnAQuestion, QnAComment

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
        return redirect('qna:answer_question')
    return render(request, 'qna/ask_question.html')

def answer_question(request):
    category = request.GET.get('category')
    if category:
        questions = QnAQuestion.objects.filter(category=category).order_by('-created_at')
    else:
        questions = QnAQuestion.objects.all().order_by('-created_at')
    return render(request, 'qna/answer_question.html', {'questions': questions, 'selected_category': category})

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
            return redirect('qna:question_detail', question_id=question_id)
    return render(request, 'qna/question_detail.html', {'question': question, 'comments': comments})

@login_required(login_url='/accounts/login_real/')
def question_history(request):
    questions = QnAQuestion.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'qna/question_history.html', {'questions': questions})
