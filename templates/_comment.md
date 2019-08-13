=============== 댓글 
======= models.py

class Comment(models.Model):
objects = models.Manager()
content = models.TextField()
user = models.ForeignKey(User, on_delete = models.CASCADE)
post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
# Post의 Comment, Comment의 Post를 서로 추적 가능

created_at = models.DateTimeField(auto_now_add=True)


======= 터미널

python manage.py makemigrations
python manage.py migrate


======= forms.py

from .models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        labels = {
            'content': "내용",
        }


======= show.html
=== posts/new_comment.html 파일 생성

<h2>댓글</h2>
<p>댓글 수 : {{ post.comments.count }}개</p> <!-- related_name을 써서 가능한 부분 -->
<a href="{% url 'posts:new_comment' post.id %}">댓글 남기기</a> <!-- url 클릭 시 post.id를 함께 넘겨줌 -->
{% for comment in post.comments.all %}
    <p>쓰니 : {{ comment.username }}</p>
    <p>내용 : {{ comment.content }}</p>
    {% empty %}
    <p>댓글이 없습니다.</p>
{% endfor %}


======= new_comment.html

<h1>댓글 달기</h1>
<form action="{% url 'posts:new_comment' post.id %}" method="POST">
    {% csrf_token %}
    <label>댓글 내용</label><br>
    <textarea name="content"></textarea><br>
    
    <input type="submit" value="댓글쓰기">
</form>


======= posts / urls.py

path('<int:id>/new_comment/', views.new_comment, name="new_comment"),


======= views.py

from .forms import PostForm, CommentForm

def new_comment(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/new_comment.html', {'post': post})
    
    
======= posts / urls.py

path('<int:id>/create_comment/', views.create_comment, name="create_comment"),


======= views.py
    
def create_comment(request, id):
    form = CommentForm()
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:show', post.id)
    return render(request, 'posts/new_comment.html', {'form': form})
    
    
======= show.html

<form action="{% url 'posts:delete_comment' comment.id %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="댓글삭제">
</form>


======= posts / urls.py

path('<int:id>', views.delete_comment, name="delete_comment"),


======= views.py

def delete_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    post = comment.post
    comment.delete()
    return render(request, 'posts/show.html', {"post": post})
