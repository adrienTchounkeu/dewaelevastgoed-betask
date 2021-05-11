from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status

from articles.models import Article, Tag
from articles.serializers import ArticleSerializer, TagSerializer


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at']


class ArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagAddRemoveAPIView(generics.RetrieveUpdateDestroyAPIView):

    # add tag to article
    def put(self, request, pk):
        article_id = request.get_params['article_id']
        tag = None
        article = None
        try:
            tag = Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            return Response("No Tag with this id", status=status.HTTP_404_NOT_FOUND)
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response("No article with this id", status=status.HTTP_404_NOT_FOUND)

        tag.article = article
        tag.save()
        return Response("Article successfully added", status=status.HTTP_200_OK)

    # remove tag from article
    def delete(self, request, pk):
        article_id = request.get_params['article_id']
        tag = None
        article = None
        try:
            tag = Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            return Response("No Tag with this id", status=status.HTTP_404_NOT_FOUND)
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response("No article with this id", status=status.HTTP_404_NOT_FOUND)

        tag.article = None
        tag.save()
        return Response("Article successfully remove", status=status.HTTP_200_OK)


class ListArticleByTag(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get(self, request, tag_id):
        tag = None
        try:
            tag = Tag.objects.get(pk=tag_id)
        except Tag.DoesNotExist:
            return Response("No Tag with this id", status=status.HTTP_404_NOT_FOUND)
        # retrieve all children tags
        articles = tag.article_set.all()
        for tag in Tag.objects.filter(parent=tag):
            articles.append(tag.article_set.all())
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

