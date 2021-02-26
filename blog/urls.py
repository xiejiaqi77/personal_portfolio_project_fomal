
from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views # this . is important

app_name = 'blog'

urlpatterns = [
    path('', views.all_blog, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

]
