from django.db import models
from django import forms
from django.contrib.auth.models import User


class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # ForeignKey: Post마다 username이 있음
    # CASCADE: User가 삭제되면 그 유저의 Post도 모두 삭제 cf. PROTECT, SET_NULL(사용자이름만 없어짐)
    likes = models.ManyToManyField(User, related_name='likes')
    # Post에 likes column을 추가
    # 1:N 관계는 ForeignKey를, M:N 관계는 ManyToManyField를 사용
    # 'likes'를 통해 User와 연결됨

    image = models.ImageField(upload_to="images/", null=True)
    likes_user_set = models.ManyToManyField(User, related_name='likes_user_set')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Comment(models.Model):
    objects = models.Manager()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    # Post의 Comment, Comment의 Post를 서로 추적 가능
    
    created_at = models.DateTimeField(auto_now_add=True)
