from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class Genres(models.Model):
    genre_id=models.AutoField(primary_key=True) 
    name = models.TextField()
    
    def __str__(self):
        return self.name
    class Meta:
        managed= False
        db_table='genres'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
    def __str__(self):
        return self.name
    class Meta:
        managed= False
        db_table='admin'
    

class Book(models.Model):  
    book_id = models.AutoField(primary_key=True) 
    title = models.TextField()
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    author = models.TextField()
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    class Meta:
        managed= False
        db_table='books'

class CustomUser(AbstractUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True) 
    name = models.TextField()
    email = models.TextField(unique=True)
    password = models.TextField()  # This should be replaced with a secure password field
    deleted = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'users'

class Borrowing(models.Model):
    borrowing_id=models.AutoField(primary_key=True) 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  
    details = models.TextField()
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=(timezone.now() + timezone.timedelta(days=30)))
    
    def __str__(self):
        return f"{self.user_id.name} borrowed {self.book.title}"
    class Meta:
        managed= False
        db_table='borrowings'
