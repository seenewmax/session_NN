from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.show, name="show"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]