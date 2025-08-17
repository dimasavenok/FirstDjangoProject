from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from blogapp.models import BlogPost


# Create your views here.
class PostListView(ListView):
    model = BlogPost
    template_name = "blogapp/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return BlogPost.objects.filter(is_publish=True)

class PostDetailView(DetailView):
    model = BlogPost
    template_name = "blogapp/post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fiels=["views_count"])

class PostCreateView(CreateView):
    model = BlogPost
    template_name = "blogapp/post_create.html"
    fields = ["title", "content", "preview", "is_publish"]
    success_url = reverse_lazy("post_list")

class PostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blogapp/post_create.html"
    fields = ["title", "content", "preview", "is_publish"]

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.pk})

class PostDeleteView(DetailView):
    model = BlogPost
    template_name = "blogapp/post_delete.html"
    success_url = reverse_lazy("post_list")

