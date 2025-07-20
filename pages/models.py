from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QnAQuestion(models.Model):
    CATEGORY_CHOICES = [
        ('mental_illness', '정신 질환 의심'),
        ('relationship', '연애 고민'),
        ('daily_life', '일상 공유'),
        ('other_advice', '기타 조언 구하기'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"

class QnAComment(models.Model):
    question = models.ForeignKey(QnAQuestion, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.first_name}: {self.content[:20]}"
