from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Book


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

def books_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug)
    return render(request, 'books/detail.html', {'book': book})
