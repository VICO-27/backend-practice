from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm  # if you are using forms later

# Home view
def home(request):
    posts = Post.objects.all()  # get all posts
    return render(request, 'blog/home.html', {'posts': posts})

# Detail view
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

# Add Post
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})
