from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 대출 상태를 위한 상수 정의
LOAN_STATUS_CHOICES = [
    ('B', '대출 중'),
    ('R', '반납됨'),
    ('O', '연체'),
]

class BookLoan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    borrower_name = models.CharField(max_length=100)
    borrowed_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS_CHOICES, default='B')

    def __str__(self):
        return f"{self.book.title} - {self.borrower_name}"
