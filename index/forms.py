from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Введите ваш email'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Добавляем CSS-классы для каждого поля
        for field_name, field in self.fields.items():
            field.label = ""
            field.help_text = None
            field.widget.attrs.update({
                'placeholder': field_name
            })

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class CustomLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         # Добавляем CSS-классы для каждого поля
#         for field_name, field in self.fields.items():
#             field.label = ""
#             field.help_text = None
#             field.widget.attrs.update({
#                 'placeholder': field_name
#             })
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#         return user

class FeedbackForm(forms.Form):
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': 10,
            'cols': 90,
            'class': 'form-control',
            'placeholder': 'Введите сообщение...',
        }),
        max_length=1000,
        required=True
    )