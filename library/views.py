from .models import Book, CustomUser, Borrowing
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

#index page
def index_view(request):
    return render(request, 'index.html')

#books
def book_all(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request,'books.html', {'books': books}) 

def delete_book (book_id):
    book=get_object_or_404(Book, book_id=book_id)
    book.deleted = True
    book.save()
    return redirect('library:book_all')

def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_details.html', {'book': book})

#users  
def user_view(request):    
    users = CustomUser.objects.all()
    return render(request, 'users.html', {'users': users})

def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, user_id=user_id)
    if request.method == 'POST':
        # Handle form submission and update user data
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('library:user_view')
    return render(request, 'edit_user.html', {'user': user})

def delete_user(user_id):
    user = get_object_or_404(CustomUser, user_id=user_id)
    user.deleted = True
    user.save()
    return redirect('library:user_view')

def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        CustomUser.objects.create(name=name, email=email)
        return redirect('library:user_view')
    return render(request, 'add_user.html')

#History
def user_history(request, user_id):
    user_borrowings = Borrowing.objects.filter(user_id=user_id)
    return render(request, 'user_history.html', {'user_borrowings': user_borrowings})

#Registration
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

#Login
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'  