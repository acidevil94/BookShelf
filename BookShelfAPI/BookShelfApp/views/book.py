from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from BookShelfApp.models import  Book
from BookShelfApp.serializers import BookSerializer

# Create your views here.
@csrf_exempt
def bookApi(request, id = 0):
    if request.method == 'GET':
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return JsonResponse(book_serializer.data, safe=False)
    
    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        else:
            return JsonResponse("Failed to add", safe=False)

    elif request.method=='PUT':
        book_data = JSONParser().parse(request)
        book = Book.objects.get(book_id=book_data['book_id'])
        book_serializer = BookSerializer(book, data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Updated Succesfully", safe=False)
        else:
            return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        book=Book.objects.get(book_id=id)
        book.delete()
        return JsonResponse("Deleted Successfully", safe=False)