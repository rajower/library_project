from django.contrib.auth import login
from .forms import EditUserForm, ContactForm, NewUserForm
from django.contrib.auth.models import User 
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from .models import Book, Borrowing
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import success
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse

#index page
def index_view(request):
    return render(request, 'index.html')

#books
def book_all(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request,'books.html', {'books': books}) 

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.deleted = True
    book.save()
    return redirect('library:book_all')


def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_details.html', {'book': book})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.availability:
        borrowing = Borrowing(id=request.user, book=book, details=f"Borrowed {book.title}")
        borrowing.save()
        book.availability = False
        book.save()
        messages.success(request, f"You have successfully borrowed {book.title}.")
        return redirect('library:user_history', user_id=request.user.id)
    else:
        messages.error(request, "This book is not available for borrowing.")
        return redirect('library:book_details', book_id=book_id)
    

#users  
def user_list(request):
    users = User.objects.filter(is_active=True)  # Exclude the logged-in user
    return render(request, 'users.html', {'users': users})


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            # Save the user type based on the selected choice
            user_type = form.cleaned_data.get('user_type')
            if user_type == 'superuser':
                user.is_superuser = True
                user.is_staff = True
            elif user_type == 'staff':
                user.is_superuser = False
                user.is_staff = True
            else:
                user.is_superuser = False
                user.is_staff = False

            # Save the other form fields
            form.save()

            return redirect('library:user_list')
    else:
        form = EditUserForm(instance=user)

    return render(request, 'edit_user.html', {'form': form, 'user_id': user_id})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    return redirect('library:user_list')

#History
@login_required
def user_history(request, user_id):
    selected_user = get_object_or_404(User, id=user_id)
    user_borrowings = Borrowing.objects.filter(id=user_id)
    return render(request, 'user_history.html', {'selected_user': selected_user, 'user_borrowings': user_borrowings})


def admin_dashboard(request):
    # Get the current date
    current_date = datetime.now().date()

    # Calculate the date one week from now
    one_week_from_now = current_date + timedelta(days=7)

    # Query for books that are due within a week
    books_due_within_week = Borrowing.objects.filter(due_date__lte=one_week_from_now)

    return render(request, 'admin_dashboard.html', {'books_due_within_week': books_due_within_week})

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
            messages.success(request, "Registration successful.")
            return redirect("library:login")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})

#contact us form 
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'], 
            }
            message = "\n".join([f"{key}: {value}" for key, value in body.items()])

            try:
                send_mail(subject, message, 'neveamore77@gmail.com', ['neveamore77@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            messages.success(request, "Email Sent! We will be in touch")
            
      
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
