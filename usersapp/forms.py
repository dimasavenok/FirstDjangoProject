from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from usersapp.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ["email", "password1", "password2"]

class CustomAuthenticationForm(AuthenticationForm):
    pass

