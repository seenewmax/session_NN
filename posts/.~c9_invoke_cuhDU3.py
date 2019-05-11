from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .forms import PostForm

def create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'posts/create.html', {'form': form})
    
def new(request):
    return render(request, 'posts/new.html')

def show(request, id):
    post = get_object_or_404(Post, id)
    return render(request, 'posts/show.html', {"post": post})
    
def update(request, id):
    post = get_object_or_404(Post, id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        post.save()
        return redirect('show', post.id)
    return render(request, 'posts/update.html', {"post": post})
    
    
def delete(request, id):
    post = get_object_or_404(Post, id)
    if request.method == "POST":
        post.delete()
        return redirect('main')