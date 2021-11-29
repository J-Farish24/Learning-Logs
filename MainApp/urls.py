from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'MainApp'
urlpatterns = [
    path('',views.index,name='index'),
    path('topics',views.topics,name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),
]