----------- 댓글 
-- models.py
    class Comment(models.Model):
    objects = models.Manager()
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
-- forms.py
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

-- views.py
    from .forms import PostForm, CommentForm
    
    def create_comment(request, id):
    form = CommentForm()
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.username = request.user
            comment.save()
            return redirect('posts:show', post.id)
    return render(request, 'posts/new_comment.html', {'form': form})
    
    def new_comment(request, id):
        post = get_object_or_404(Post, pk=id)
        return render(request, 'posts/new_comment.html', {'post': post})

-- show.html
    <h2>댓글</h2>
    <p>댓글 수 : {{ post.comments.count }}개</p>
    <a href="{% url 'posts:new_comment' post.id %}">댓글 남기기</a>
    {% for comment in post.comments.all %}
        <p>쓰니 : {{ comment.username }}</p>
        <p>내용 : {{ comment.content }}</p>
        {% empty %}
        <p>댓글이 없습니다.</p>
    {% endfor %}

-- urls.py
    path('<int:id>/new_comment/', views.new_comment, name="new_comment"),
    path('<int:id>/create_comment/', views.create_comment, name="create_comment"),
    
-- new_comment.html
    <h1>댓글 달기</h1>
    <form action="{% url 'posts:create_comment' post.id %}" method="POST">
        {% csrf_token %}
        <label>댓글 내용</label><br>
        <textarea name="content"></textarea><br>
        
        <input type="submit" value="댓글쓰기">
    </form>