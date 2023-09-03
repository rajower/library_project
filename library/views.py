from django.contrib.auth import login
from django.contrib.auth.models import User 
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Book, Borrowing
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib import messages


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
def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def edit_user(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('library:user_view')
    return render(request, 'users/edit_user.html', {'user': user})

def delete_user(user_id):
    user = get_object_or_404(User, user_id=user_id)
    user.deleted = True
    user.save()
    return redirect('library:user_view')

#History
def user_history(request, user_id):
    user_borrowings = Borrowing.objects.filter(user_id=user_id)
    return render(request, 'user_history.html', {'user_borrowings': user_borrowings})

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def user_home(request):
    return render(request, 'user_home.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('library:user_home')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("library:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})