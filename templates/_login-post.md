--------로그인
-- 터미널
    pipenv install django-allauth

-- project.url
    path('accounts/', include('allauth.urls')),

-- settings.py 위
    'django.contrib.sites', # new
    'allauth', # new
    'allauth.account', # new
    'allauth.socialaccount', # new
    'allauth.socialaccount.providers.github', # new

-- settings.py 아래
    ACCOUNT_EMAIL_VERIFICATION = 'none'
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )
    SITE_ID = 1
    LOGIN_REDIRECT_URL = 'home'
    LOGOUT_REDIRECT_URL = 'home'

-- home.html
    {% if user.is_authenticated %}
      안녕 {{ user.username }}!
    <a href="{% url 'account_logout' %}">logout</a>
    <a href="{% url 'posts:new' %}">새 글 쓰기</a>
    <p>===========================</p>
    {% for post in posts %}
        <a href="{% url 'posts:show' post.id %}"><h2>#{{ post.id }} : {{ post.title }}</h2></a>
        <p>쓰니: {{ post.username }}</p>
        <p>===========================</p>
        {% empty %}
        <p>글이 없습니다.</p>
    {% endfor %}
    
    {% else %}
      <p>You are not logged in</p>
      <a href="{% url 'account_login' %}">login</a>
    {% endif %}
    
    
--------포스트에 유저 달기
-- models.py
    from django.contrib.auth.models import User
    
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    
-- views.py / def create
    from django.contrib.auth.models import User
    
    form = form.save(commit=False)
    form.username = request.user