from django.urls import path
from . import views

app_name = 'library'  # Set the app namespace

urlpatterns = [
    path('', views.index_view, name='index'),  # Home page
    path('login/', views.CustomLoginView.as_view(), name='login'), 
    path('register/', views.register_view, name='register'),
    path('users/', views.user_view, name='user_view'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('users/add/', views.add_user, name='add_user'),
    path('books/<int:book_id>/', views.book_details, name='book_details'), 
    path('books/', views.book_all, name='book_all'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('users/<int:user_id>/history/', views.user_history, name='user_history'),
    # Add other URL patterns as needed
]
