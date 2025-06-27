from django.contrib.auth.forms import UserCreationForm as BaseUserCreaeionForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

# User 모델 
User = get_user_model()

# 회원 가임 form
class CreateUser(BaseUserCreaeionForm):
    email = forms.EmailField( # 기존 form 구성에 없는 email 추가.
        label='이메일',
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete':'email'})
    )
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if (
            username
            and self._meta.model.objects.filter(username__iexact=username).exists()
        ):
            raise ValidationError(
                self.instance.unique_error_message(self._meta.model, ['username'])
            )
        return username # 유효성 검사 통과 시, clean_data 반영
    class Meta(BaseUserCreaeionForm): # 기존 UserCreationForm의 Meta Class 상속 받아 사용.
        model = User
        fields = ('username', 'email', 'password1', 'password2') # 이메일 추가
