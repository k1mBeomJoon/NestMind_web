from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class UserProfileForm(forms.ModelForm):
    nickname = forms.CharField(max_length=30, required=False, label='닉네임')

    class Meta:
        model = User
        fields = ('username', 'email', 'nickname', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            try:
                self.fields['nickname'].initial = self.instance.profile.nickname
            except Profile.DoesNotExist:
                self.fields['nickname'].initial = ''

    def save(self, commit=True):
        user = super().save(commit)
        nickname = self.cleaned_data.get('nickname')
        if user.pk:
            profile, created = Profile.objects.get_or_create(user=user)
            profile.nickname = nickname
            profile.save()
        return user

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname')
    search_fields = ('nickname', 'user__username')

# UserAdmin에 Profile.nickname을 표시
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = '프로필'

class UserAdmin(BaseUserAdmin):
    form = UserProfileForm
    # inlines = (ProfileInline,)  # Profile 인라인 제거
    # '이름'(first_name), '성'(last_name) 대신 '닉네임'만 보이도록 list_display 수정
    list_display = tuple(x for x in BaseUserAdmin.list_display if x not in ('first_name', 'last_name')) + ('get_nickname',)
    search_fields = BaseUserAdmin.search_fields + ('profile__nickname',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('개인정보', {'fields': ('nickname', 'email', 'first_name', 'last_name')}),
        ('권한', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('중요 날짜', {'fields': ('last_login', 'date_joined')}),
    )

    def get_nickname(self, obj):
        return obj.profile.nickname if hasattr(obj, 'profile') else ''
    get_nickname.short_description = '닉네임'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
