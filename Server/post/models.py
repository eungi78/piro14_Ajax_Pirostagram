from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='포스트 제목')
    image = models.ImageField(blank=True, upload_to='post', verbose_name='이미지')
    content = models.TextField(verbose_name='내용')
    like_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str(self):
        return self.content
