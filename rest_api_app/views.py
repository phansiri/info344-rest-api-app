from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_api_app.models import Books
from rest_api_app.serializers import UsersSerializer
from rest_api_app.forms import BookForm

@api_view(['GET', 'POST'])
def book_list(request, format=None):
    """
    List all users, or create a new user
    """
    if request.method == 'GET':
        users = Books.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET',))
def book_root(request, format=None):
    return Response({
        'Books': reverse('book_list', request=request, format=format)
    })

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk, format=None):
    """
    Retrieve, update or delete a user instance
    """
    try:
        user = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def post_list(request):
    books = Books.objects.order_by('title')
    return render(request, 'rest_api_app/post_list.html', {'books': books})

def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book.save()
            return redirect('rest_api_app.views.book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'rest_api_app/book_edit.html', {'form': form})
