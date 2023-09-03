from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('user_home/', views.user_home, name='user_home'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('books/<int:book_id>/', views.book_details, name='book_details'),
    path('books/', views.book_all, name='book_all'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('users/<int:user_id>/history/', views.user_history, name='user_history'),
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Add the login URL here
    path('register/', views.register_request, name='register'),  # Add the registration URL here
    # Other app-specific URLs
]
