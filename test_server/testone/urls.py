from django.urls import path
from .views import access_test, get_book, create_book, update_book, create_author, create_language, create_genre

app_name = 'testone'

urlpatterns = [
    path('access-test/', access_test, name="access_test"),

    path('books/<book_id>', get_book, name="get_book"),
    path('books/<book_id>/', update_book, name="update_book"),
    path('book/', create_book, name="create_book"),

    path('author/', create_author, name="create_author"),
    path('language/', create_language, name="create_language"),
    path('genre/', create_genre, name="create_genre")
]