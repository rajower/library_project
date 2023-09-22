from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('logout/', auth_views.LogoutView.as_view(next_page='library:index'), name='logout'),
    path('register/', views.register_request, name='register'), 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('books/<int:book_id>/borrow/', views.borrow_book, name='borrow_book'),
    path("contact", views.contact, name='contact'),
    path('success/',views.success, name='success'),
    # Other app-specific URLs
]
