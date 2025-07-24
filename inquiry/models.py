from django.db import models
from django.contrib.auth.models import User

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
