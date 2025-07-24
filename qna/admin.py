from django.contrib import admin
from .models import QnAQuestion, QnAComment

class QnACommentInline(admin.TabularInline):
    model = QnAComment
    extra = 1
    fields = ('author', 'content', 'created_at')
    readonly_fields = ('created_at',)
    show_change_link = True

@admin.register(QnAQuestion)
class QnAQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'created_at', 'short_content')
    list_display_links = ('title',)
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
    list_display_links = ('short_content',)
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
