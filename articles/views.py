from rest_framework import generics

from articles.models import Article
from articles.serializers import ArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at']


class ArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
