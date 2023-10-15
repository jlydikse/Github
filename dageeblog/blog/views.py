from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_description(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_description.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_description', pk=post.pk)
        else:
            return HttpResponseBadRequest("Form submission is invalid.")
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    