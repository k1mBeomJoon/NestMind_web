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

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('pages:question_detail', kwargs={'question_id': self.id})

class QnAComment(models.Model):
    question = models.ForeignKey(QnAQuestion, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.first_name}: {self.content[:20]}"

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Inquiry(models.Model):
    CATEGORY_CHOICES = [
        ('operation', '운영 관련'),
        ('privacy', '개인정보 관련'),
        ('report', '신고 관련'),
        ('other', '기타 문의'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inquiries')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title} - {self.user.username}"

class LoveTypeQuestion(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text

class LoveTypeTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='love_type_results')
    answers = models.JSONField()
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    test_type = models.CharField(max_length=30, default='love_type')
    def __str__(self):
        return f"{self.user.username} - {self.test_type} - {self.score}점"

class EmotionStyleQuestion(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text

class EmotionStyleTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emotion_style_results')
    answers = models.JSONField()
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    test_type = models.CharField(max_length=30, default='emotion_style')
    def __str__(self):
        return f"{self.user.username} - {self.test_type} - {self.score}점"

class PersonalityQuestion(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text

class PersonalityTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personality_results')
    answers = models.JSONField()
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    test_type = models.CharField(max_length=30, default='personality')
    def __str__(self):
        return f"{self.user.username} - {self.test_type} - {self.score}점"

class MentalHealthQuestion(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text

class MentalHealthTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mental_health_results')
    answers = models.JSONField()
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    test_type = models.CharField(max_length=30, default='mental_health')
    def __str__(self):
        return f"{self.user.username} - {self.test_type} - {self.score}점"

class ReportType(models.Model):
    TYPE_CODE_CHOICES = [
        ('ASCX', 'ASCX'), ('ASCI', 'ASCI'), ('ASOX', 'ASOX'), ('ASOI', 'ASOI'),
        ('ABCX', 'ABCX'), ('ABCI', 'ABCI'), ('ABOX', 'ABOX'), ('ABOI', 'ABOI'),
        ('RSCX', 'RSCX'), ('RSCI', 'RSCI'), ('RSOX', 'RSOX'), ('RSOI', 'RSOI'),
        ('RBCX', 'RBCX'), ('RBCI', 'RBCI'), ('RBOX', 'RBOX'), ('RBOI', 'RBOI'),
    ]
    type_code = models.CharField(max_length=8, choices=TYPE_CODE_CHOICES, unique=True)
    type_name = models.CharField(max_length=100)
    description = models.TextField()
    traits = models.TextField()
    problems = models.TextField()
    recommendations = models.TextField()
    character_image = models.ImageField(upload_to='report_characters/', blank=True, null=True)

    def __str__(self):
        return f"{self.type_code} : {self.type_name}"

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.report_type.type_code} - {self.created_at.strftime('%Y-%m-%d')}"
