from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


## 1-1 Relationship
# 1 user can have only one profile => 1
# 1 profile is owned by only one user => N
# OneToOneField()=> Any model

## 1-M Relationship
#1 user can add multiple post =>M
#1 post is added by only one user =>1
# in django use ForeignKey()=> use in many side Model

## M -M relationship
# 1 student can learn from multiple teachers => M
# 1 teacher can teach multiple students
# MAnyToManyField => Any Place
