from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    post_date = models.DateField()

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_date = models.DateField()
