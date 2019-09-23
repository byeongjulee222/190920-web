from django.urls import path
from . import views

app_name='eithers'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'), 
    path('<int:question_pk>/', views.detail, name='detail'),
    path('<int:question_pk>/comment/', views.answer_create, name='answer_create'),
    path('<int:question_pk>/comment/<int:answer_pk>/delete/', views.comment_delete, name='comment_delete'),
]

