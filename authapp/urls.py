from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('quiz/start/', views.start_quiz, name='start_quiz'),  
    path('quiz/question/<int:question_id>/', views.quiz_question, name='quiz_question'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
]
