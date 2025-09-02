from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib import messages

from usersapp.forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.
class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "usersapp/register.html"
    success_url = reverse_lazy("usersapp:login")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Регистрация прошла успешно")
        return super().form_valid(form)

class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "usersapp/login.html"

    def get_success_url(self):
        return reverse_lazy("catalog:home")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("catalog:home"))