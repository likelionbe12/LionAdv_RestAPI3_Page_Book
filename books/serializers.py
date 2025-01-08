from rest_framework import serializers
from .models import Category, Book, BookLoan

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'category',
                 'category_name', 'publication_date', 'price',
                 'stock', 'created_at', 'updated_at']

class BookLoanSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = BookLoan
        fields = ['id', 'book', 'book_title', 'borrower_name',
                 'borrowed_date', 'due_date', 'return_date', 'status']
