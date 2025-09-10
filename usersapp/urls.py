from django.urls import path

from usersapp.views import UserLoginView, logout, UserRegisterView

app_name = "usersapp"
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]