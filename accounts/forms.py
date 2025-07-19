from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    nickname = forms.CharField(max_length=30, required=True, label='닉네임')

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "nickname")

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        
        if not password:
            raise forms.ValidationError("패스워드를 입력해주세요.")
        
        if len(password) < 8:
            raise forms.ValidationError("패스워드는 8글자 이상이어야 합니다.")
        
        # 영문/한글과 숫자 혼합 확인
        has_letter = bool(re.search(r'[a-zA-Z가-힣]', password))
        has_number = bool(re.search(r'\d', password))
        
        if not (has_letter and has_number):
            raise forms.ValidationError("패스워드는 영문/한글과 숫자를 혼합해야 합니다.")
        
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['nickname']  # nickname을 first_name에 저장
        if commit:
            user.save()
        return user