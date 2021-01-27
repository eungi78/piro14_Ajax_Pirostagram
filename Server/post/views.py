from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, 'post/base.html', ctx)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save()
            return redirect('post:post_list')
    else:
        form = PostForm()
    return render(request, "post/post_create.html", {'form': form})


def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        content = request.POST['comment']  # comment의 content 가져오기
        comment = Comment.objects.create(post=post, content=content)
        comment.save()
        return redirect('post:post_list')

def like(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        if post.like_status is False:
            Post.objects.filter(pk=post_pk).update(like_status=True)
        else:
            Post.objects.filter(pk=post_pk).update(like_status=False)
    return redirect('post:post_list')

def comment_delete(request, post_pk, comment_pk):
    post=Post.objects.get(pk=post_pk)
    comment=post.comment_set.get(pk=comment_pk)
    if request.method =='POST':
        comment.delete()
        return redirect('post:post_list')
    else:
        return redirect('post:post_list')