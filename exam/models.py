from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
