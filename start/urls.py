from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('articlecreate/', ArticleCreate.as_view(), name='articlecreate'),
    path('videocreate/', VideoCreate.as_view(), name='videocreate'),
    path('commentcreate/<str:content_type>/<int:object_id>/', CommentCreate.as_view(), name='commentcreate'),   
]
