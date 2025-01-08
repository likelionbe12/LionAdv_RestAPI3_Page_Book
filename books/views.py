from rest_framework import viewsets
from rest_framework import filters
from .models import Category, Book, BookLoan
from .serializers import CategorySerializer, BookSerializer, BookLoanSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'isbn', 'category__name']
    ordering_fields = ['title', 'author', 'publication_date', 'price']

    def get_queryset(self):
        queryset = Book.objects.all()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category_id=category)
        return queryset

class BookLoanViewSet(viewsets.ModelViewSet):
    queryset = BookLoan.objects.all()
    serializer_class = BookLoanSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['borrower_name', 'book__title']
    ordering_fields = ['borrowed_date', 'due_date', 'status']

    def get_queryset(self):
        queryset = BookLoan.objects.all()
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        return queryset
