from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class DateTimeField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TitleClass(DateTimeField):
    title = models.CharField(max_length=30)
    
    class Meta:
        abstract = True

class Article(TitleClass):    
    text = models.CharField(max_length=200)
    comments = GenericRelation('Comment')
    
    def __str__(self):
        return self.title
    
class Video(TitleClass):    
    video = models.URLField(max_length=200)
    comments = GenericRelation('Comment')
    
    def __str__(self):
        return self.title

class Comment(DateTimeField):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    text = models.TextField() 
