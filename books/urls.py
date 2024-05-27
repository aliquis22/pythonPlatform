from django.contrib import admin
from django.urls import path
from books.views import books_list, books_detail
from django.conf.urls.static import static
from django.conf import settings
app_name = 'books'

urlpatterns = [
    path('', books_list, name='books'),
    path('book/<int:id>', books_detail, name='detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)