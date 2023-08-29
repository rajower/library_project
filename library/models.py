from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Genres(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'genres'

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
        managed = False
        db_table = 'books'

class Borrowing(models.Model):
    borrowing_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    details = models.TextField()
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=(timezone.now() + timezone.timedelta(days=30)))

    def __str__(self):
        return f"{self.user.name} borrowed {self.book.title}"
    class Meta:
        managed = False
        db_table = 'borrowings'



