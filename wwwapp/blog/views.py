from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

# from django.shortcuts import render

# def test(request, imie, wiek):
#     template_data = {
#         't_imie': imie,
#         't_wiek': wiek,
#     }
#     return render(request, 'blog/test.html', template_data)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})