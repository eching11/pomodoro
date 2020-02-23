from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Added from Django Tutorial part 5
    path('categories/', views.CategoryListView.as_view(), name='category'),
    path('category/<uuid:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('pomodoros/', views.PomodoroListView.as_view(), name='pomodoro'),
    path('pomodoro/<uuid:pk>', views.PomodoroDetailView.as_view(), name='pomodoro-detail'),
    path('mypomodoros/', views.PomodoroByUserListView.as_view(), name='my-pomodoros'),
]

# Add edit-pomodoro page
from timer import views
urlpatterns += [
    path('pomodoro/<str:pk>/edit_pomodoro/', views.edit_pomodoro, name='edit_pomodoro'),
]

# Add create, update, and delete operations
urlpatterns += [
    path('pomodoro/create/', views.PomodoroCreate.as_view(), name='pomodoro_create'),
    path('pomodoro/<uuid:pk>/update', views.PomodoroUpdate.as_view(), name='pomodoro_update'),
    path('pomodoro/<uuid:pk>/delete', views.PomodoroDelete.as_view(), name='pomodoro_delete'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<uuid:pk>/update', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<uuid:pk>/delete', views.CategoryDelete.as_view(), name='category_delete'),
]