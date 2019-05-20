sudo pip3 install pipenv
pipenv install django
pipenv shell

===============로그인
======= 터미널

pipenv install django-allauth


======= settings.py INSTALLED_APPS

'django.contrib.sites', # new
'allauth', # new
'allauth.account', # new
'allauth.socialaccount', # new
'allauth.socialaccount.providers.github', # new


======= settings.py 맨 아래

# 로그인 시 유저네임으로 로그인 (or email)
ACCOUNT_AUTHENTICATION_METHOD = 'username'
# 회원가입 시 이메일 입력 필수 여부
ACCOUNT_EMAIL_REQUIRED = False
# 회원가입 시 이메일 인증 관련 코드
ACCOUNT_EMAIL_VERIFICATION = 'none'

AUTHENTICATION_BACKENDS = (
    # 쟝고 superuser로 로그인 가능
    "django.contrib.auth.backends.ModelBackend",
    
    # 이메일 등으로 로그인 가능
    "allauth.account.auth_backends.AuthenticationBackend",
)
SITE_ID = 1
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


======= project.url

path('accounts/', include('allauth.urls')),


======= home.html

{% if user.is_authenticated %}
  안녕 {{ user.user }}!
<a href="{% url 'account_logout' %}">logout</a>
<a href="{% url 'posts:new' %}">새 글 쓰기</a>
<p>===========================</p>
{% for post in posts %}
    <a href="{% url 'posts:show' post.id %}"><h2>#{{ post.id }} : {{ post.title }}</h2></a>
    <p>쓰니: {{ post.user }}</p>
    <p>===========================</p>
    {% empty %}
    <p>글이 없습니다.</p>
{% endfor %}

{% else %}
  <p>You are not logged in</p>
  <a href="{% url 'account_login' %}">login</a>
{% endif %}


======= 터미널

python manage.py migrate


===============포스트에 유저 달기
======= models.py

from django.contrib.auth.models import User

user = models.ForeignKey(User, on_delete = models.CASCADE)
# ForeignKey: Post마다 user가 있음
# CASCADE: User가 삭제되면 그 유저의 Post도 모두 삭제 cf. PROTECT, SET_NULL


======= 터미널

python manage.py makemigrations
python manage.py migrate


======= views.py / def create

from django.contrib.auth.models import User

form = form.save(commit=False) # form을 당장 저장하지 않음. 데이터 저장 전 뭔가 하고 싶을 때 사용.
form.user = request.user