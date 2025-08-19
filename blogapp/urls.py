from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView


app_name = "blogapp"
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
]