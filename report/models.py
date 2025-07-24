from django.db import models
from django.contrib.auth.models import User

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
