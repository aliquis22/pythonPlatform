from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Book
from reviews.forms import ReviewForm
from reviews.models import Review
def books_list(request, section_slug=None):
    section = None
    sections = Section.objects.all()
    if section_slug:
        section = get_object_or_404(Section, slug=section_slug)
        books = section.books.all()  # Получаем все книги из соответствующего раздела
    else:
        books = Book.objects.all()  # Если раздел не указан, получаем все книги
    return render(request, 'books/books_list.html',
                  {
                      'section': section,
                      'books': books
                  })


def books_detail(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = book.reviews.all()
    average_rating = book.average_rating()
    user_review = Review.objects.filter(book=book, user=request.user).first()
    if request.method == 'POST':
        if 'delete_review' in request.POST:
            review = get_object_or_404(Review, id=request.POST.get('delete_review'), user=request.user)
            review.delete()
            return redirect('books:detail', id=id)

        if user_review:
            form = ReviewForm(request.POST, instance=user_review)
        else:
            form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('books:detail', id=id)
    else:
        form = ReviewForm(instance=user_review) if user_review else ReviewForm()
    return render(request, 'books/detail.html', {'book': book, 'reviews': reviews, 'form': form, 'average_rating': average_rating, 'user_review': user_review})
