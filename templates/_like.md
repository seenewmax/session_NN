=============== 좋아요
======= posts / models.py / class Post

likes = models.ManyToManyField(User, related_name='likes')
# Post에 likes column을 추가
# 1:N 관계는 ForeignKey를, M:N 관계는 ManyToManyField를 사용
# 'likes'를 통해 User와 연결됨


======= 터미널

python manage.py makemigrations
python manage.py migrate


======= posts / urls.py

path('<int:id>/like/', views.like, name="like"),


======= views.py

def like(request, id):
    user = request.user #로그인한 유저를 가져옴
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        if post.likes.filter(id = user.id).exists(): #해당 post에 로그인한 유저가 like 컬럼에 존재하면
            post.likes.remove(user) #like 컬럼에서 해당 유저를 지운다.
        else:
            post.likes.add(user) #그 외의 경우 추가한다.
    return redirect('posts:show', post.id)
    
    
======= show.html

<form action="{% url 'posts:like' post.id%}" method="POST">
    {% csrf_token %}
    <input type="submit" value="좋아요">
</form>
{{ post.likes.count }}개


======= show.html

좋아요 누른 사람
{% for user in post.likes.all %}
{{ user.username }}
{% empty %}
없음
{% endfor %}
