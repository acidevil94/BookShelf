from rest_framework import serializers
from BookShelfApp.models import User, Book, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id',
                 'user_name')



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_id',
                 'book_name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_id',
                 'post_user',
                 'post_book',
                 'post_date')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_id',
                 'comment_user',
                 'comment_post',
                 'comment_date')