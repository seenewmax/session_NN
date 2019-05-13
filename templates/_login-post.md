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
      Hi {{ user.username }}!
    <a href="{% url 'account_logout' %}">logout</a>
    <a href="{% url 'posts:new' %}">새 글 쓰기</a>
    
    {% for post in all_posts %}
        <p>{{ post.title }}</p>
        <p>{{ post.content }}</p>
        <p>{{ post.created_at }}</p>
        <a href="{% url 'posts:show' post.id %}">보러가기</a>
        <p>===========================</p>
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