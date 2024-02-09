from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from .forms import CreatePostForm, UpdatePostForm
# Create your views here.
def index(request):

    return render(request, 'index.html')

def posts(request):
    posts = models.Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})

def more(request, pk):
    post = models.Post.objects.get(id = pk)
    return render(request, 'more.html', {'post':post})

def delete(request, pk):
    post = models.Post.objects.get(id = pk)
    post.delete()
    messages.success(request,"با موفقیت حذف شد")
    return redirect('posts')

def form(request):

    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            models.Post.objects.create(title=cd['title'], text=cd['text'], author=cd['author'], cover=cd['cover'])
            messages.success(request, "پست شما با موفقیت انتشار یافت")
            return redirect('posts')
    else:
        form = CreatePostForm()
    return render(request, 'form.html', {'form':form})



def edit(request, pk):

    post = models.Post.objects.get(id = pk)
    if request.method == 'POST':
        form = UpdatePostForm(request.POST, request.FILES, instance= post)
        if form.is_valid():
            form.save()
            messages.success(request, "پست شما با موفقیت ویرایش شد ")
            return redirect('posts')
        

    form = UpdatePostForm(instance = post)
    return render(request, 'edit.html',{'form':form} )
