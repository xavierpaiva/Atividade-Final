from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    addres = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todo(models.Model):
    userld = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField()

class Post(models.Model):
    userld = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.IntegerField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    postld = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100) 
    body = models.IntegerField()

    def __str__(self):
        return self.name