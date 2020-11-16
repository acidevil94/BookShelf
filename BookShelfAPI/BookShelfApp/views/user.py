from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from BookShelfApp.models import User, Book, Post, Comment
from BookShelfApp.serializers import UserSerializer, BookSerializer, PostSerializer, CommentSerializer

# Create your views here.
@csrf_exempt
def userApi(request, id = 0):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        else:
            return JsonResponse("Failed to add", safe=False)

    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user=User.objects.get(user_id=user_data['user_id'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Succesfully", safe=False)
        else:
            return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        user=User.objects.get(user_id=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)