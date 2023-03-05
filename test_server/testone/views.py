from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

from .models import Book, Author, Language, Genre


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def access_test(request):
    res_data = {}

    msg = 'TEST ACCESS API'
    res_data['message'] = msg
    print('access_test')

    return Response(data=res_data, status=status.HTTP_200_OK)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def create_book(request):
    try:
        res_data = {}

        book_title = request.data.get('title')
        book_summary = request.data.get('summary')
        book_isbn = request.data.get('isbn')
        book_author_first_name = request.data.get('first_name')
        book_author_last_name = request.data.get('last_name')
        book_language = request.data.get('language')
        book_genre = request.data.get('genre').split(',')

        author = Author.objects.get(first_name=book_author_first_name, last_name=book_author_last_name)
        language = Language.objects.get(name=book_language)

        book_info = Book.objects.create(
            title=book_title,
            summary=book_summary,
            isbn=book_isbn,
            author=author,
            language_id=language.pk
        )
        for gen in book_genre:
            genre = Genre.objects.get(name=gen.strip())
            book_info.genre.add(genre)

        msg = 'POST BOOK INFO'
        res_data['message'] = msg
        res_data['book_id'] = book_info.pk

        return Response(data=res_data, status=status.HTTP_200_OK)
    except Exception as ex:
        print('ex:', ex)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_book(request, book_id):
    try:
        res_data = {}
        if request.method == 'GET':
            msg = 'GET BOOK INFO'
            res_data['message'] = msg

            book_info = Book.objects.get(pk=int(book_id))

            res_data['title'] = book_info.title
            res_data['summary'] = book_info.summary
            res_data['isbn'] = book_info.isbn

            gen_list = []
            book_genre = book_info.genre.all()
            for gen in book_genre:
                gen_list.append(gen.name)
            res_data['genre'] = gen_list

            if not book_info.author:
                res_data['author'] = None
            else:
                res_data['author'] = book_info.author.first_name + ' ' + book_info.author.last_name

            if not book_info.language:
                res_data['language'] = None
            else:
                res_data['language'] = book_info.language.name

        return Response(data=res_data, status=status.HTTP_200_OK)
    except Exception as ex:
        print('ex:', ex)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(('PUT', 'DELETE'))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def update_book(request, book_id):
    res_data = {}
    try:
        if request.method == 'PUT':
            msg = 'UPDATE BOOK INFO'
            res_data['message'] = msg

            book_info = Book.objects.get(pk=int(book_id))
            book_info.summary = request.data.get('summary')
            book_info.save()

        elif request.method == 'DELETE':
            msg = 'DELETE BOOK INFO'
            res_data['message'] = msg

            book_info = Book.objects.get(pk=int(book_id))

            book_info.genre.remove(*book_info.genre.all())
            book_info.delete()

        return Response(data=res_data, status=status.HTTP_200_OK)
    except Exception as ex:
        print('ex:', ex)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def create_author(request):
    try:
        res_data = {}

        author_last_name = request.data.get('last_name')
        author_first_name = request.data.get('first_name')

        author_info = Author.objects.create(
            last_name=author_last_name,
            first_name=author_first_name,
        )

        msg = 'POST AUTHOR INFO'
        res_data['message'] = msg
        res_data['author_id'] = author_info.pk

        return Response(data=res_data, status=status.HTTP_200_OK)
    except Exception as ex:
        print('ex:', ex)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def create_language(request):
    try:
        res_data = {}

        language_name = request.data.get('name')

        language_info = Language.objects.create(
            name=language_name
        )

        msg = 'POST LANGUAGE INFO'
        res_data['message'] = msg
        res_data['language_id'] = language_info.pk

        return Response(data=res_data, status=status.HTTP_200_OK)
    except Exception as ex:
        print('ex:', ex)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def create_genre(request):
    try:
        res_data = {}

        genre_name = request.data.get('name')

        genre_info = Genre.objects.create(
            name=genre_name
        )

        msg = 'POST GENRE INFO'
        res_data['message'] = msg
        res_data['genre_id'] = genre_info.pk

        return Response(data=res_data, status=status.HTTP_200_OK)
    except Exception as ex:
        print('ex:', ex)
        return Response(status=status.HTTP_400_BAD_REQUEST)