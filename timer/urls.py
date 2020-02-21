from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Added from Django Tutorial part 5
    path('categories/', views.CategoryListView.as_view(), name='category'),
    path('category/<str:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('pomodoros/', views.PomodoroListView.as_view(), name='pomodoro'),
    path('pomodoro/<str:pk>', views.PomodoroDetailView.as_view(), name='pomodoro-detail'),
    path('mypomodoros/', views.PomodoroByUserListView.as_view(), name='my-pomodoros'),
]
