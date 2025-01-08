from django.core.management.base import BaseCommand
from django.utils import timezone
from books.models import Category, Book, BookLoan
from faker import Faker
import random
from decimal import Decimal
from datetime import timedelta

fake = Faker("ko_KR")

class Command(BaseCommand):
    help = 'Generates dummy data for the library system'

    def handle(self, *args, **kwargs):
        self.stdout.write('Generating dummy data...')

        # 카테고리 생성
        categories = [
            '소설', '과학', '역사', '예술', '철학',
            '기술', '경제', '자기계발', '여행', '요리'
        ]

        category_objects = []
        for cat_name in categories:
            category = Category.objects.create(
                name=cat_name,
                description=fake.paragraph()
            )
            category_objects.append(category)

        self.stdout.write(f'Created {len(categories)} categories')

        # 도서 생성
        for _ in range(100):  # 100권의 책 생성
            published_date = fake.date_between(start_date='-10y', end_date='today')

            book = Book.objects.create(
                title=fake.catch_phrase(),
                author=fake.name(),
                isbn=fake.unique.random_number(digits=13),
                category=random.choice(category_objects),
                publication_date=published_date,
                price=Decimal(random.uniform(10.0, 100.0)).quantize(Decimal('0.01')),
                stock=random.randint(0, 20)
            )

        self.stdout.write('Created 100 books')

        # 대출 기록 생성
        books = Book.objects.all()

        for _ in range(200):  # 200개의 대출 기록 생성
            book = random.choice(books)
            borrowed_date = fake.date_between(start_date='-1y', end_date='today')
            due_date = borrowed_date + timedelta(days=14)
            status = random.choice(['B', 'R', 'O'])

            return_date = None
            if status in ['R', 'O']:
                if status == 'R':
                    return_date = borrowed_date + timedelta(days=random.randint(1, 14))
                else:  # Overdue
                    return_date = due_date + timedelta(days=random.randint(1, 30))

            BookLoan.objects.create(
                book=book,
                borrower_name=fake.name(),
                borrowed_date=borrowed_date,
                due_date=due_date,
                return_date=return_date,
                status=status
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated dummy data'))
