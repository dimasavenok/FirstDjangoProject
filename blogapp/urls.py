from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView


app_name = "catalog"
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail')

]