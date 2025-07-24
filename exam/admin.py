from django.contrib import admin
from .models import LoveTypeQuestion, LoveTypeTestResult, EmotionStyleQuestion, EmotionStyleTestResult, PersonalityQuestion, PersonalityTestResult, MentalHealthQuestion, MentalHealthTestResult

admin.site.register(LoveTypeQuestion)
admin.site.register(LoveTypeTestResult)
admin.site.register(EmotionStyleQuestion)
admin.site.register(EmotionStyleTestResult)
admin.site.register(PersonalityQuestion)
admin.site.register(PersonalityTestResult)
admin.site.register(MentalHealthQuestion)
admin.site.register(MentalHealthTestResult)
