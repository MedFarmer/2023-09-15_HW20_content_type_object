from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import *
from django.forms import ModelForm
from django.urls import reverse_lazy

class Home(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('__all__')

class ArticleCreate(CreateView):
    form_class = ArticleForm
    template_name = 'article_create.html'
    success_url = reverse_lazy('home')

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ('__all__')

class VideoCreate(CreateView):
    form_class = VideoForm
    template_name = 'video_create.html'
    success_url = reverse_lazy('home')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_create.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        
        content_type = self.kwargs.get('content_type')
        object_id = self.kwargs.get('object_id')                
        content_model = ContentType.objects.get(model=content_type).model_class()
        content_object = content_model.objects.get(pk=object_id)                
        comment = form.save(commit=False)
        comment.content_object = content_object
        comment.save()
        return super().form_valid(form)
    


