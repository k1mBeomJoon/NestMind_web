from django.contrib import admin
from .models import QnAQuestion, QnAComment, FAQ, Notice, Inquiry, LoveTypeQuestion, LoveTypeTestResult, EmotionStyleQuestion, EmotionStyleTestResult, PersonalityQuestion, PersonalityTestResult, MentalHealthQuestion, MentalHealthTestResult

class QnACommentInline(admin.TabularInline):
    model = QnAComment
    extra = 1
    fields = ('author', 'content', 'created_at')
    readonly_fields = ('created_at',)
    show_change_link = True

@admin.register(QnAQuestion)
class QnAQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'created_at', 'short_content')
    list_display_links = ('title',)  # 제목을 클릭하면 상세로 이동
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content', 'author__username', 'author__first_name')
    inlines = [QnACommentInline]
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'author', 'content')
        }),
        ('날짜 정보', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    def short_content(self, obj):
        return obj.content[:30] + ('...' if len(obj.content) > 30 else '')
    short_content.short_description = '본문 미리보기'

@admin.register(QnAComment)
class QnACommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'author', 'created_at', 'short_content')
    list_display_links = ('short_content',)  # 미리보기를 클릭하면 상세로 이동
    search_fields = ('content', 'author__username', 'author__first_name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('question', 'author', 'content')
        }),
        ('날짜 정보', {
            'fields': ('created_at',),
        }),
    )
    def short_content(self, obj):
        return obj.content[:30] + ('...' if len(obj.content) > 30 else '')
    short_content.short_description = '댓글 미리보기'

admin.site.register(FAQ)
admin.site.register(Notice)

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'title', 'created_at', 'answer')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content', 'user__username')
    readonly_fields = ('content', 'answer')

admin.site.register(Inquiry, InquiryAdmin)

class LoveTypeQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at')
    search_fields = ('text',)

class LoveTypeTestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'score', 'created_at', 'test_type')
    list_filter = ('test_type', 'created_at')
    search_fields = ('user__username',)

class EmotionStyleQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at')
    search_fields = ('text',)

class EmotionStyleTestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'score', 'created_at', 'test_type')
    list_filter = ('test_type', 'created_at')
    search_fields = ('user__username',)

class PersonalityQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at')
    search_fields = ('text',)

class PersonalityTestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'score', 'created_at', 'test_type')
    list_filter = ('test_type', 'created_at')
    search_fields = ('user__username',)

class MentalHealthQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at')
    search_fields = ('text',)

class MentalHealthTestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'score', 'created_at', 'test_type')
    list_filter = ('test_type', 'created_at')
    search_fields = ('user__username',)

admin.site.register(LoveTypeQuestion, LoveTypeQuestionAdmin)
admin.site.register(LoveTypeTestResult, LoveTypeTestResultAdmin)
admin.site.register(EmotionStyleQuestion, EmotionStyleQuestionAdmin)
admin.site.register(EmotionStyleTestResult, EmotionStyleTestResultAdmin)
admin.site.register(PersonalityQuestion, PersonalityQuestionAdmin)
admin.site.register(PersonalityTestResult, PersonalityTestResultAdmin)
admin.site.register(MentalHealthQuestion, MentalHealthQuestionAdmin)
admin.site.register(MentalHealthTestResult, MentalHealthTestResultAdmin)
